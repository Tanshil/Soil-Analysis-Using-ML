import streamlit as st
import pandas as pd
import joblib
import os

# Load model and scaler (assumes models/ exists from run_training.py)
MODEL_DIR = "models"
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")

@st.cache_resource
def load_model():
    model_files = [f for f in os.listdir(MODEL_DIR) if f.endswith('_model.pkl')]
    if not model_files:
        st.error("No trained model found. Run `python src/run_training.py` first!")
        st.stop()
    best_model_path = os.path.join(MODEL_DIR, model_files[0])
    try:
        scaler = joblib.load(SCALER_PATH)
    except Exception as e:
        st.error(f"Scaler load failed: {str(e)}. Run training first.")
        st.stop()
    
    model = joblib.load(best_model_path)
    return model, scaler, best_model_path

def preprocess_input(input_df, scaler, model):
    # Replicate training preprocessing
    X_encoded = pd.get_dummies(input_df, columns=["Soil Type", "Crop Type"], prefix=["Soil", "Crop"])
    
    # Match training: Moisture qcut for single row (fixed bins ~tertiles)
    X_encoded["Moisture_level"] = pd.cut(X_encoded["Moisture"], bins=[0, 33.333, 66.667, 100], labels=["Low", "Medium", "High"])
    X_encoded = pd.get_dummies(X_encoded, columns=["Moisture_level"], prefix="Moisture")
    
    # Add features matching training
    if "Nitrogen" in X_encoded and "Phosphorous" in X_encoded and "Potassium" in X_encoded:
        X_encoded["NPK_total"] = X_encoded["Nitrogen"] + X_encoded["Phosphorous"] + X_encoded["Potassium"]
    if "Temperature" in X_encoded and "Humidity" in X_encoded:
        X_encoded["Temp_Humidity"] = X_encoded["Temperature"] * X_encoded["Humidity"]
    # Do not use qcut on single-row inference input.
    # Moisture one-hot columns are handled by reindexing to model feature columns.

    to_scale = ["Temperature", "Humidity", "Moisture", "Nitrogen", "Potassium", "Phosphorous", "NPK_total", "Temp_Humidity"]
    to_scale = [c for c in to_scale if c in X_encoded.columns]
    X_scaled = scaler.transform(X_encoded[to_scale].values.reshape(1, -1))
    X_encoded[to_scale] = X_scaled

    # Align with training-time feature set to avoid shape/column mismatch
    if hasattr(model, "feature_names_in_"):
        X_encoded = X_encoded.reindex(columns=model.feature_names_in_, fill_value=0.0)

    return X_encoded

st.title("🌱 Soil Fertilizer Recommender")
st.markdown("Upload soil data or input values. Trained on 8000 samples.")

model, scaler, model_path = load_model()
st.info(f"Loaded: {os.path.basename(model_path)}")

# Input form
col1, col2 = st.columns(2)
with col1:
    temp = st.number_input("Temperature", 0.0, 50.0, 25.0)
    hum = st.number_input("Humidity", 0.0, 100.0, 50.0)
    moist = st.number_input("Moisture", 0.0, 100.0, 30.0)
with col2:
    n = st.number_input("Nitrogen", 0.0, 100.0, 20.0)
    p = st.number_input("Phosphorous", 0.0, 100.0, 30.0)
    k = st.number_input("Potassium", 0.0, 100.0, 25.0)
    soil = st.selectbox("Soil Type", ["Clayey", "Sandy", "Loamy", "Black", "Red"])
    crop = st.selectbox(
        "Crop Type",
        ["Maize", "Sugarcane", "Cotton", "Tobacco", "Wheat", "Paddy", "Millets", "Oil seeds", "Pulses", "Ground Nuts", "Barley"],
    )

input_data = pd.DataFrame({
    "Temperature": [temp], "Humidity": [hum], "Moisture": [moist],
    "Nitrogen": [n], "Phosphorous": [p], "Potassium": [k],
    "Soil Type": [soil], "Crop Type": [crop]
})

if st.button("Recommend Fertilizer"):
    try:
        processed = preprocess_input(input_data, scaler, model)
        prediction = model.predict(processed)[0]
        probs = model.predict_proba(processed)[0] if hasattr(model, 'predict_proba') else None
        
        st.success(f"**Recommended: {prediction}**")
        if probs is not None:
            st.bar_chart(pd.Series(probs, index=model.classes_))
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        st.error("Debug: Check model/data compatibility. Run `python src/run_training.py` locally.")

# Train button
if st.button("Train New Model"):
    os.system("python src/run_training.py")
    st.success("Training complete! Refresh page.")

st.markdown("---")
st.caption("Portable ML app. Run: `streamlit run app.py`")
