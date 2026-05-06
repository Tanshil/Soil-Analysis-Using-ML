@echo off
REM Cross-platform setup for Soil Analysis ML Project (Windows CMD)

echo === Soil Analysis ML Project - Environment Setup ===

REM Check if virtual environment exists
if exist venv (
    echo [OK] Virtual environment found
) else (
    echo [!] Virtual environment not found. Creating...
    python -m venv venv
    echo [OK] Virtual environment created
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing requirements...
python -m pip install -r requirements.txt

REM Verify core packages
echo === Verifying ML Packages ===
for %%p in (pandas numpy scikit-learn matplotlib seaborn scipy jupyter ipykernel) do (
    echo %%p & python -c "import %%p" >nul 2>&1 && echo [OK] %%p || echo [!] %%p NOT INSTALLED
)

REM Check data
if exist data\data\raw\data_core.csv (
    echo [OK] Data file found
    python -c "import pandas as pd; print(pd.read_csv('data/data/raw/data_core.csv').shape)"
) else (
    echo [!] Data file not found
)

echo.
echo === Setup Summary ===
echo [OK] Setup complete!
echo To activate later: venv\Scripts\activate.bat
echo To deactivate: deactivate

pause

