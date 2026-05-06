#!/bin/bash
# Cross-platform setup for Soil Analysis ML Project
# Works on Linux, Mac, Windows (Git Bash/WSL)

set -e  # Exit on error

echo "=== Soil Analysis ML Project - Environment Setup ==="

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "[OK] Virtual environment found"
else
    echo "[!] Virtual environment not found. Creating..."
    python3 -m venv venv || python -m venv venv
    echo "[OK] Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate  # Linux/Mac
# On Windows Git Bash, this works too

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Verify core packages
echo "=== Verifying ML Packages ==="
packages=("pandas" "numpy" "scikit-learn" "matplotlib" "seaborn" "scipy" "jupyter" "ipykernel")
all_ok=true
for pkg in "${packages[@]}"; do
    python -c "import $pkg" 2>/dev/null && echo "[OK] $pkg" || { echo "[!] $pkg NOT INSTALLED"; all_ok=false; }
done

# Check data
if [ -f "data/data/raw/data_core.csv" ]; then
    echo "[OK] Data file found"
    python -c "import pandas as pd; print(pd.read_csv('data/data/raw/data_core.csv').shape)"
else
    echo "[!] Data file not found"
fi

# Summary
echo "=== Setup Summary ==="
if [ "$all_ok" = true ]; then
    echo "[OK] All core packages installed!"
else
    echo "[!] Some packages missing. Check above."
fi

echo "Setup complete!"
echo "To activate later: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate.bat (Windows CMD)"
echo "To deactivate: deactivate"

