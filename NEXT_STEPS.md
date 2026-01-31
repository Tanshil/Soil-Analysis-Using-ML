# Next Steps for Soil Analysis ML Project

## ✅ Completed
- [x] Environment setup
- [x] Data preprocessing pipeline
- [x] Feature scaling (numeric columns)
- [x] GitHub repository setup

## 🎯 Recommended Next Steps

### Step 1: Exploratory Data Analysis (EDA)
**Create:** `src/eda.ipynb`

**What to explore:**
- Data distribution (histograms, box plots)
- Target variable distribution (Fertilizer Name counts)
- Correlation between numeric features
- Relationship between categorical features and target
- Missing values check
- Outlier detection

**Key questions to answer:**
- How many unique fertilizer types?
- Which fertilizers are most common?
- Are there strong correlations between features?
- How do soil types and crop types relate to fertilizer choice?

### Step 2: Feature Engineering
**Update:** `src/preprocessing.ipynb` or create `src/feature_engineering.ipynb`

**Tasks:**
- **Encode categorical variables:**
  - `Soil Type` → One-hot encoding or Label encoding
  - `Crop Type` → One-hot encoding or Label encoding
- **Create new features (optional):**
  - NPK ratio (Nitrogen:Phosphorous:Potassium)
  - Temperature-Humidity interaction
  - Soil moisture categories

### Step 3: Train-Test Split
**Add to preprocessing pipeline:**
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_processed, y, test_size=0.2, random_state=42, stratify=y
)
```

### Step 4: Model Training
**Create:** `src/train_model.ipynb`

**Models to try:**
1. **Random Forest Classifier** (good for mixed data types)
2. **XGBoost Classifier** (high performance)
3. **Logistic Regression** (baseline)
4. **Support Vector Machine** (SVM)

### Step 5: Model Evaluation
**Metrics to use:**
- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix
- Classification Report

### Step 6: Model Selection & Hyperparameter Tuning
- Use GridSearchCV or RandomizedSearchCV
- Cross-validation
- Select best model

### Step 7: Save Model & Create Prediction Pipeline
- Save trained model (pickle/joblib)
- Create prediction function
- Test on new data

## 📝 Quick Start: EDA

Here's a template to get started with EDA:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.preprocessing import preprocess_pipeline

# Load and preprocess
DATA_PATH = "../data/data/raw/data_core.csv"
TARGET_COL = "Fertilizer Name"

df = pd.read_csv(DATA_PATH)
X_processed, y, scaler = preprocess_pipeline(DATA_PATH, TARGET_COL)

# Basic info
print("Dataset Info:")
print(df.info())
print("\nTarget Distribution:")
print(y.value_counts())

# Visualizations
plt.figure(figsize=(12, 8))
y.value_counts().plot(kind='bar')
plt.title('Fertilizer Distribution')
plt.show()
```

## 🎯 Priority Order

1. **EDA** (Understand your data) ← **START HERE**
2. **Feature Engineering** (Encode categoricals)
3. **Train-Test Split**
4. **Model Training**
5. **Evaluation & Tuning**

---

**Your next immediate step:** Create `src/eda.ipynb` and start exploring your data!
