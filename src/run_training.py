"""Run model training pipeline for Soil Analysis."""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import warnings
import os

warnings.filterwarnings('ignore')

# Optional XGBoost
try:
    from xgboost import XGBClassifier
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(_SCRIPT_DIR, "..", "data", "data", "raw", "data_core.csv")
TARGET_COL = "Fertilizer Name"

# Load and prepare data
print("Loading data...")
df = pd.read_csv(DATA_PATH)
df = df.fillna(df.mean(numeric_only=True)).fillna("Unknown")
X = df.drop(columns=[TARGET_COL])
y = df[TARGET_COL]

# Encode categoricals
X_encoded = pd.get_dummies(X, columns=["Soil Type", "Crop Type"], prefix=["Soil", "Crop"])

# Add new features
X_fe = X_encoded.copy()
X_fe["NPK_total"] = X_fe["Nitrogen"] + X_fe["Phosphorous"] + X_fe["Potassium"]
X_fe["Temp_Humidity"] = X_fe["Temperature"] * X_fe["Humidity"]
X_fe["Moisture_level"] = pd.qcut(X_fe["Moisture"], q=3, labels=["Low", "Medium", "High"])
X_fe = pd.get_dummies(X_fe, columns=["Moisture_level"], prefix="Moisture")

# Scale
to_scale = ["Temperature", "Humidity", "Moisture", "Nitrogen", "Potassium", "Phosphorous", "NPK_total", "Temp_Humidity"]
to_scale = [c for c in to_scale if c in X_fe.columns]
scaler = StandardScaler()
X_fe[to_scale] = scaler.fit_transform(X_fe[to_scale])

# Split
X_train, X_test, y_train, y_test = train_test_split(X_fe, y, test_size=0.2, random_state=42, stratify=y)
print(f"Training: {X_train.shape[0]} | Test: {X_test.shape[0]} | Features: {X_train.shape[1]}\n")

# Models
models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
    "Logistic Regression": LogisticRegression(random_state=42, max_iter=1000, n_jobs=-1),
    "SVM": SVC(random_state=42, probability=True),
}
if HAS_XGBOOST:
    models["XGBoost"] = XGBClassifier(random_state=42, eval_metric='mlogloss')
else:
    print("(XGBoost skipped - pip install xgboost for full comparison)\n")

# Train
trained = {}
for name, model in models.items():
    print(f"Training {name}...")
    model.fit(X_train, y_train)
    trained[name] = model
    print(f"  Done.\n")

# Evaluate
print("=" * 50)
print("MODEL COMPARISON")
print("=" * 50)
results = []
for name, model in trained.items():
    y_pred = model.predict(X_test)
    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, average='weighted'),
        "Recall": recall_score(y_test, y_pred, average='weighted'),
        "F1": f1_score(y_test, y_pred, average='weighted'),
    })

results_df = pd.DataFrame(results).sort_values('Accuracy', ascending=False)
print(results_df.to_string(index=False))

best_name = results_df.iloc[0]["Model"]
best_model = trained[best_name]
print(f"\nBest model: {best_name}")
print("\nClassification Report:")
print(classification_report(y_test, best_model.predict(X_test)))

# Save
_models_dir = os.path.join(_SCRIPT_DIR, "..", "models")
os.makedirs(_models_dir, exist_ok=True)
model_path = os.path.join(_models_dir, f"{best_name.lower().replace(' ', '_')}_model.pkl")
scaler_path = os.path.join(_models_dir, "scaler.pkl")
import joblib
joblib.dump(best_model, model_path)
joblib.dump(scaler, scaler_path)
print(f"\nSaved: {model_path}")
print(f"Saved: {scaler_path}")
