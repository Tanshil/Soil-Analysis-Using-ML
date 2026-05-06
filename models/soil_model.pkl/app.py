import os

import joblib
import numpy as np
import pandas as pd
import streamlit as st


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Soil Analysis & Fertilizer Recommendation",
    page_icon="🌱",
    layout="centered",
)

st.title("🌱 Soil Analysis & Fertilizer Recommendation System")
st.markdown("Provide soil and environmental parameters to get a fertilizer recommendation.")


# -----------------------------
# Paths & Constants
# -----------------------------
BASE_DIR = os.path.dirname(__file__)  # .../models/soil_model.pkl
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "data", "raw", "data_core.csv")
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")

# Prefer a generic best-model file if present, fallback to legacy logistic regression model
BEST_MODEL_PATH = os.path.join(MODELS_DIR, "best_model.pkl")
LEGACY_MODEL_PATH = os.path.join(MODELS_DIR, "logistic_regression_model.pkl")
SCALER_PATH = os.path.join(MODELS_DIR, "scaler.pkl")

TARGET_COL = "Fertilizer Name"

# Optional: map raw label values from the dataset
# to more user-friendly display names. Edit this as you like.
FERTILIZER_DISPLAY_MAP = {
    "10-26-26": "NPK Fertilizer (10-26-26)",
    "14-35-14": "NPK Fertilizer (14-35-14)",
    "17-17-17": "NPK Fertilizer (17-17-17)",
    "20-20": "NPK Fertilizer (20-20)",
    "28-28": "NPK Fertilizer (28-28)",
    "DAP": "DAP (Diammonium Phosphate)",
    "Urea": "Urea",
}
TO_SCALE = [
    "Temperature",
    "Humidity",
    "Moisture",
    "Nitrogen",
    "Potassium",
    "Phosphorous",
    "NPK_total",
    "Temp_Humidity",
]


# -----------------------------
# Model & Feature Loader
# -----------------------------
@st.cache_resource
def load_artifacts():
    """
    Load trained model + scaler and infer the full feature column set
    using the same feature-engineering steps as in training.
    """
    # Select model path
    model_path = BEST_MODEL_PATH if os.path.exists(BEST_MODEL_PATH) else LEGACY_MODEL_PATH

    if not os.path.exists(model_path):
        st.error(
            "Model file not found.\n\n"
            "Make sure you have trained the model first by running:\n"
            "`python src/run_training.py` from the project root."
        )
        st.stop()

    if not os.path.exists(SCALER_PATH):
        st.error(
            "Scaler file not found.\n\n"
            "Make sure you have trained the model first by running:\n"
            "`python src/run_training.py` from the project root."
        )
        st.stop()

    # Load trained artifacts
    model = joblib.load(model_path)
    scaler = joblib.load(SCALER_PATH)

    # Derive feature_columns from the raw dataset using the same steps
    if not os.path.exists(DATA_PATH):
        st.error(
            "Data file not found at expected location:\n"
            f"`{DATA_PATH}`\n\n"
            "Check that the dataset is available before running the app."
        )
        st.stop()

    df = pd.read_csv(DATA_PATH)
    df = df.fillna(df.mean(numeric_only=True)).fillna("Unknown")

    X = df.drop(columns=[TARGET_COL])

    # Encode categoricals as in feature_engineering / training
    X_encoded = pd.get_dummies(X, columns=["Soil Type", "Crop Type"], prefix=["Soil", "Crop"])

    # Add engineered features (same as training)
    X_fe = X_encoded.copy()
    X_fe["NPK_total"] = X_fe["Nitrogen"] + X_fe["Phosphorous"] + X_fe["Potassium"]
    X_fe["Temp_Humidity"] = X_fe["Temperature"] * X_fe["Humidity"]

    # In training, an additional Moisture_level one-hot encoding was added.
    # For inference we do NOT need to recreate it for a single row because
    # we will simply leave these columns as zeros (if present) when we
    # reindex to the full training column set.
    X_fe["Moisture_level"] = pd.qcut(
        X_fe["Moisture"],
        q=3,
        labels=["Low", "Medium", "High"],
    )
    X_fe = pd.get_dummies(X_fe, columns=["Moisture_level"], prefix="Moisture")

    feature_columns = X_fe.columns.tolist()

    return model, scaler, feature_columns


def prepare_features_single(
    temperature: float,
    humidity: float,
    moisture: float,
    soil_type: str,
    crop_type: str,
    nitrogen: float,
    potassium: float,
    phosphorous: float,
    scaler,
    feature_columns,
) -> pd.DataFrame:
    """
    Take raw user input and transform it into the feature vector expected by the model.

    This mirrors the training feature engineering:
    - one-hot encode Soil Type and Crop Type
    - add NPK_total and Temp_Humidity
    - scale numeric features with the saved scaler
    - align columns to training feature set (missing columns filled with 0)
    """
    raw_df = pd.DataFrame(
        [
            {
                "Temperature": temperature,
                "Humidity": humidity,
                "Moisture": moisture,
                "Soil Type": soil_type,
                "Crop Type": crop_type,
                "Nitrogen": nitrogen,
                "Potassium": potassium,
                "Phosphorous": phosphorous,
            }
        ]
    )

    # One-hot encode categoricals
    encoded = pd.get_dummies(raw_df, columns=["Soil Type", "Crop Type"], prefix=["Soil", "Crop"])

    # Engineered features (same formulas as training)
    encoded["NPK_total"] = encoded["Nitrogen"] + encoded["Phosphorous"] + encoded["Potassium"]
    encoded["Temp_Humidity"] = encoded["Temperature"] * encoded["Humidity"]

    # NOTE: We intentionally do NOT compute Moisture_level bins here.
    # The training data had Moisture_Low / Medium / High one-hot columns;
    # for a single new sample, we simply keep those columns at 0 when we
    # reindex to the training feature_columns. This keeps the column
    # layout consistent while avoiding fragile quantile binning logic.

    # Align columns with training feature space
    X_single = encoded.reindex(columns=feature_columns, fill_value=0.0)

    # Scale numeric columns with the saved scaler
    to_scale_present = [c for c in TO_SCALE if c in X_single.columns]
    if to_scale_present:
        X_single[to_scale_present] = scaler.transform(X_single[to_scale_present])

    return X_single


# Load artifacts once per session
model, scaler, feature_columns = load_artifacts()


# -----------------------------
# Input Section
# -----------------------------
st.subheader("🔢 Input Soil & Environmental Parameters")

col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("Temperature (°C)", min_value=-20.0, max_value=60.0, value=25.0, step=0.5)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=1.0)
    moisture = st.number_input("Soil Moisture", min_value=0.0, value=40.0, step=1.0)
    nitrogen = st.number_input("Nitrogen (N)", min_value=0.0, value=20.0, step=1.0)

with col2:
    phosphorous = st.number_input("Phosphorous (P)", min_value=0.0, value=20.0, step=1.0)
    potassium = st.number_input("Potassium (K)", min_value=0.0, value=20.0, step=1.0)

    soil_type = st.selectbox(
        "Soil Type",
        options=["Sandy", "Clayey", "Loamy", "Red", "Black"],
    )
    crop_type = st.selectbox(
        "Crop Type",
        options=[
            "Maize",
            "Sugarcane",
            "Cotton",
            "Tobacco",
            "Paddy",
            "Wheat",
            "Barley",
            "Millets",
            "Pulses",
            "Oil seeds",
            "Ground Nuts",
        ],
    )


# -----------------------------
# Prediction
# -----------------------------
st.markdown("---")

if st.button("🔍 Predict Fertilizer"):
    try:
        features = prepare_features_single(
            temperature=temperature,
            humidity=humidity,
            moisture=moisture,
            soil_type=soil_type,
            crop_type=crop_type,
            nitrogen=nitrogen,
            potassium=potassium,
            phosphorous=phosphorous,
            scaler=scaler,
            feature_columns=feature_columns,
        )

        prediction = model.predict(features)
        # Convert to string to be safe with NumPy / pandas types
        raw_label = str(prediction[0])
        display_name = FERTILIZER_DISPLAY_MAP.get(raw_label, raw_label)

        st.success(f"✅ Recommended Fertilizer: **{display_name}**")
        if raw_label != display_name:
            st.caption(f"(Dataset label: `{raw_label}`)")

    except Exception as e:
        st.error(f"Prediction failed: {e}")


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built using Machine Learning & Streamlit")
