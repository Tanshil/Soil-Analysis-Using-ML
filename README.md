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
│   └── preprocess.ipynb            # Data preprocessing notebook
├── venv/                           # Virtual environment (created by setup)
├── requirements.txt                # Python dependencies
├── setup_environment.ps1           # Environment setup script
├── activate_env.ps1                # Quick activation script
└── README.md                       # This file
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

2. Open your notebook:
   ```powershell
   jupyter notebook src/preprocess.ipynb
   ```

3. Make sure to select the correct kernel in your notebook (should be "Python (Soil Analysis)" or your system Python)

## Troubleshooting

### Jupyter Kernel Issues

If you encounter kernel connection issues, see `KERNEL_TROUBLESHOOTING.md` or run:
```powershell
.\fix_kernel.ps1
```

### Package Import Errors

If you get import errors:
1. Make sure the virtual environment is activated
2. Verify packages are installed: `python -m pip list`
3. Reinstall requirements: `python -m pip install -r requirements.txt`

## Next Steps

- [ ] Explore and visualize the dataset
- [ ] Perform data preprocessing and feature engineering
- [ ] Train ML models for fertilizer recommendation
- [ ] Evaluate model performance
- [ ] Create prediction pipeline

## Notes

- Always activate the virtual environment before working on the project
- The dataset is located at `data/data/raw/data_core.csv`
- Use Jupyter notebooks for exploratory data analysis and model development
