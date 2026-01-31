# Soil Analysis ML Project

Machine Learning project for soil analysis and fertilizer recommendation.

## Project Structure

```
Soil Analysis/
├── data/
│   └── data/
│       └── raw/
│           └── data_core.csv      # Main dataset (8000 rows, 9 columns)
├── src/
│   ├── preprocessing.ipynb        # Data preprocessing pipeline
│   └── eda.ipynb                  # Exploratory data analysis
├── venv/                          # Virtual environment (created by setup)
├── setup_environment.ps1           # Environment setup script
├── activate_env.ps1               # Quick activation script
├── NEXT_STEPS.md                  # Recommended next steps (feature engineering, training)
├── QUICK_START.md                 # Quick start guide
└── README.md                      # This file
```

## Dataset

The dataset contains 8000 samples with the following features:
- **Temperature**: Soil temperature
- **Humidity**: Humidity level
- **Moisture**: Soil moisture content
- **Soil Type**: Type of soil
- **Crop Type**: Type of crop
- **Nitrogen**: Nitrogen content
- **Potassium**: Potassium content
- **Phosphorous**: Phosphorous content
- **Fertilizer Name**: Target variable (fertilizer recommendation)

## Environment Setup

### Prerequisites
- Python 3.10.2 or higher
- PowerShell (Windows)

### Quick Start

1. **Run the setup script** (first time only):
   ```powershell
   .\setup_environment.ps1
   ```

2. **Activate the virtual environment**:
   ```powershell
   .\activate_env.ps1
   ```
   Or manually:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. **Start Jupyter Notebook**:
   ```powershell
   jupyter notebook
   ```
   Or JupyterLab:
   ```powershell
   jupyter lab
   ```

### Manual Setup

If you prefer to set up manually:

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Register Jupyter kernel (optional)
python -m ipykernel install --user --name soil-analysis --display-name "Python (Soil Analysis)"
```

## Key Libraries

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms
- **matplotlib**: Plotting and visualization
- **seaborn**: Statistical data visualization
- **scipy**: Scientific computing
- **jupyter**: Interactive notebook environment

## Usage

1. Activate the environment:
   ```powershell
   .\activate_env.ps1
   ```

2. Open a notebook:
   ```powershell
   jupyter notebook src/eda.ipynb
   jupyter notebook src/preprocessing.ipynb
   ```
   Or open the `src/` folder in VS Code/Cursor and run cells in either notebook.

3. **EDA** (`src/eda.ipynb`): Run cells in order — Load Data, then Dataset Overview, Data Quality Checks, Categorical Analysis, Numerical Distributions, Correlation Analysis.

4. Select the correct kernel in your notebook (e.g. "Python (Soil Analysis)" or your venv Python).

## Troubleshooting

### Jupyter Kernel Issues

- Ensure the virtual environment is activated before starting Jupyter.
- In the notebook, choose the kernel that points to your project’s Python (e.g. the venv or "Python (Soil Analysis)" if registered).

### Package Import Errors

If you get import errors:
1. Activate the virtual environment: `.\activate_env.ps1`
2. Check installed packages: `python -m pip list`
3. Reinstall dependencies: run `.\setup_environment.ps1` again or install manually (pandas, matplotlib, seaborn, scikit-learn, jupyter).

## Next Steps

- [x] Environment setup
- [x] Data preprocessing pipeline (`src/preprocessing.ipynb`)
- [x] Exploratory data analysis (`src/eda.ipynb`)
- [ ] Feature engineering (encode categoricals, optional new features)
- [ ] Train–test split and model training
- [ ] Evaluation and prediction pipeline

See **NEXT_STEPS.md** for detailed steps and code snippets.

## Notes

- Always activate the virtual environment before working on the project.
- Dataset path: `data/data/raw/data_core.csv` (from project root); in `src/` notebooks use `../data/data/raw/data_core.csv`.
- **EDA** covers: overview, quality checks, categorical value counts, numerical histograms, and correlation heatmap.
- For the full roadmap (feature engineering, models, evaluation), see **NEXT_STEPS.md**.
