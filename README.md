=======
# 🌱 Soil Analysis Using Machine Learning

An end-to-end machine learning project designed to analyze soil characteristics and predict soil categories for agricultural optimization. This project demonstrates a complete ML pipeline — from data preprocessing and model training to evaluation and (optionally) deployment-ready architecture.

---

## 🚀 Problem Statement

Soil quality plays a critical role in agricultural productivity. Traditional soil analysis methods are time-consuming and require manual expertise.

This project aims to:

* Automate soil classification using machine learning
* Enable faster and more scalable soil assessment
* Support data-driven agricultural decision-making

---

## 🧠 Solution Overview

The system takes soil parameters as input and predicts the soil category using trained machine learning models.

### Workflow:

1. Data Collection & Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training (multiple algorithms)
5. Model Evaluation & Selection
6. Prediction Pipeline

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** scikit-learn, pandas, numpy, matplotlib, seaborn
* **Modeling:** Supervised Machine Learning Algorithms
* **Environment:** Jupyter Notebook / Python Scripts

---

## 📊 Machine Learning Models Used

The following models were implemented and compared:

* Logistic Regression
* Random Forest
* Support Vector Machine (SVM) *(if applicable)*
* (Add any additional model you used)

### Model Selection Strategy

The final model was selected based on performance metrics such as accuracy, precision, recall, and F1-score.

---

## 📉 Visualizations

The project includes:

* Feature importance analysis
* Correlation heatmaps
* Confusion matrix
* Data distribution plots

---

## 📂 Project Structure

```
Soil Analysis/
├── data/
│   └── data/
│       └── raw/
│           └── data_core.csv      # Main dataset (8000 rows, 9 columns)
├── src/
│   ├── preprocessing.ipynb        # Data preprocessing pipeline
│   ├── eda.ipynb                  # Exploratory data analysis
│   ├── feature_engineering.ipynb  # Feature engineering
│   ├── preprocess.ipynb           # Additional preprocessing
│   ├── train_model.ipynb          # Model training experiments
│   ├── train_model_executed.ipynb # Executed training notebook
│   └── run_training.py            # Production training script
├── models/
│   ├── soil_model.pkl             # Primary trained model
│   ├── logistic_regression_model.pkl
│   └── scaler.pkl
├── app.py                         # Streamlit/Flask app (if deployed)
├── requirements.txt
├── setup.sh / setup.bat           # Environment setup
├── activate.sh / activate.bat     # Environment activation
├── README.md
├── QUICK_START.md
├── NEXT_STEPS.md
└── TODO.md
```

---

## ⚙️ How to Run

### Prerequisites
- Python 3.8+

### Quick Start (Cross-Platform)

1. **Run setup** (first time):
   - **Linux/Mac/Git Bash**: `./setup.sh`
   - **Windows CMD**: `setup.bat`

2. **Activate environment**:
   - **Linux/Mac/Git Bash**: `source activate.sh`
   - **Windows CMD**: `activate.bat`

3. **Run Jupyter**:
   ```
   jupyter notebook
   # Open src/eda.ipynb or src/preprocessing.ipynb
   ```

### Manual Setup (if needed)

```bash
python -m venv venv
# Activate as above
pip install -r requirements.txt
```

---

## 🔌 API Usage (if app.py deployed)

**Run:** `streamlit run app.py` or `python app.py`

**Endpoint (POST /predict):**

Input:
```json
{
  "nitrogen": 50,
  "phosphorus": 30,
  "potassium": 40,
  "ph": 6.5,
  "temperature": 25,
  "humidity": 60,
  "rainfall": 100
}
```

Output:
```json
{
  "soil_type": "Loamy"
}
```

---

## 🌍 Real-World Impact

* Enables faster soil classification
* Helps farmers make better crop decisions
* Reduces dependency on manual soil testing

---

## 🔮 Future Improvements

* Deploy as web app (Streamlit completed in app.py)
* Real-time soil sensor integration
* Deep learning models
* Dataset expansion

---

## 👨‍💻 Author

**Tanshil Tigran**

---

## 📜 License

MIT License

---

=======
Soil Analysis/
├── data/
│   └── data/
│       └── raw/
│           └── data_core.csv      # Main dataset (8000 rows, 9 columns)
├── src/
│   ├── preprocessing.ipynb        # Data preprocessing pipeline
│   └── eda.ipynb                  # Exploratory data analysis
├── venv/                          # Virtual environment (created by setup)
├── setup.sh             # Cross-platform setup (Linux/Mac/Windows Git Bash)
├── setup.bat            # Windows CMD setup
├── activate.sh          # Cross-platform activation (Linux/Mac/Windows Git Bash)
├── activate.bat         # Windows CMD activation
├── NEXT_STEPS.md                  # Recommended next steps (feature engineering, training)
├── QUICK_START.md                 # Quick start guide
└── README.md                      # This file
>>>>>>> 1c57cf3 (Add all local project files: app.py, notebooks, scripts, models, data, TODO.md, requirements.txt, setup/activate scripts; update README and other docs; remove old PS1 scripts)
```

---

## ⚙️ How to Run

### 1. Clone the repository

<<<<<<< HEAD
```bash
git clone https://github.com/Tanshil/Soil-Analysis-Using-ML.git
cd Soil-Analysis-Using-ML
=======
### Prerequisites
- Python 3.8+

### Quick Start (Cross-Platform)

1. **Run setup** (first time):
   - **Linux/Mac/Git Bash**: `./setup.sh`
   - **Windows CMD**: `setup.bat`

2. **Activate environment**:
   - **Linux/Mac/Git Bash**: `source activate.sh` or `source venv/bin/activate`
   - **Windows CMD**: `activate.bat` or `venv\Scripts\activate.bat`
   - **Windows PowerShell** (optional): `venv\Scripts\Activate.ps1`

3. **Run Jupyter**:
   ```
   jupyter notebook
   # or
   jupyter lab
   ```

**Note**: On Windows, use CMD or Git Bash for best compatibility. PowerShell works with manual activation.

### Manual Setup

If you prefer to set up manually:

```bash
# Create virtual environment
python -m venv venv

# Activate (platform-specific)
# Linux/Mac: source venv/bin/activate
# Windows CMD: venv\\Scripts\\activate.bat
# Windows PowerShell: venv\\Scripts\\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Register Jupyter kernel (optional)
python -m ipykernel install --user --name soil-analysis --display-name "Python (Soil Analysis)"
>>>>>>> 1c57cf3 (Add all local project files: app.py, notebooks, scripts, models, data, TODO.md, requirements.txt, setup/activate scripts; update README and other docs; remove old PS1 scripts)
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the training pipeline

<<<<<<< HEAD
```bash
python src/train.py
```

### 4. Make predictions
=======
1. Activate environment (see Quick Start above)

2. Open notebook:
   ```
   jupyter notebook src/eda.ipynb
   ```
   Or open the `src/` folder in VS Code/Cursor and run cells in either notebook.
>>>>>>> 1c57cf3 (Add all local project files: app.py, notebooks, scripts, models, data, TODO.md, requirements.txt, setup/activate scripts; update README and other docs; remove old PS1 scripts)

```bash
python src/predict.py
```

---

## 🔌 (Optional) API Usage

If deployed with FastAPI/Flask:

**Endpoint:**

```
POST /predict
```

<<<<<<< HEAD
**Input:**
=======
If you get import errors:
1. Activate environment (see Quick Start)
2. Check: `python -m pip list`
3. Reinstall: `./setup.sh` (Linux/Mac) or `setup.bat` (Windows)
>>>>>>> 1c57cf3 (Add all local project files: app.py, notebooks, scripts, models, data, TODO.md, requirements.txt, setup/activate scripts; update README and other docs; remove old PS1 scripts)

```json
{
  "nitrogen": 50,
  "phosphorus": 30,
  "potassium": 40,
  "ph": 6.5
}
```

<<<<<<< HEAD
**Output:**
=======
- [x] Cross-platform environment setup
- [x] Data preprocessing (`src/preprocessing.ipynb`)
- [x] EDA (`src/eda.ipynb`)
- [x] Training script (`src/run_training.py`)
- [ ] Feature engineering notebook
- [ ] Model serving
>>>>>>> 1c57cf3 (Add all local project files: app.py, notebooks, scripts, models, data, TODO.md, requirements.txt, setup/activate scripts; update README and other docs; remove old PS1 scripts)

```json
{
  "soil_type": "Loamy"
}
```

---

## 🌍 Real-World Impact

* Enables faster soil classification
* Helps farmers make better crop decisions
* Reduces dependency on manual soil testing

---

## 🔮 Future Improvements

* Deploy as a web application (Streamlit / React + API)
* Integrate real-time soil sensor data
* Use deep learning for higher accuracy
* Expand dataset for better generalization

---

## 👨‍💻 Author

**Tanshil Tigran**

* B.Tech CSE (AI & ML)
* Passionate about Machine Learning & Scalable Systems

---

## ⭐ Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---
