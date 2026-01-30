# Soil Analysis ML Project - Environment Setup Script
# This script verifies and sets up the environment for the soil analysis ML project

Write-Host "=== Soil Analysis ML Project - Environment Setup ===" -ForegroundColor Green
Write-Host ""

# Check if virtual environment exists
if (Test-Path "venv") {
    Write-Host "[OK] Virtual environment found" -ForegroundColor Green
} else {
    Write-Host "[!] Virtual environment not found. Creating..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "[OK] Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "`nActivating virtual environment..." -ForegroundColor Cyan
& ".\venv\Scripts\Activate.ps1"

# Check Python version
Write-Host "`n=== Python Environment ===" -ForegroundColor Cyan
$pythonVersion = python --version
Write-Host "Python version: $pythonVersion" -ForegroundColor White

# Check pip version
$pipVersion = python -m pip --version
Write-Host "Pip version: $pipVersion" -ForegroundColor White

# Verify core ML packages
Write-Host "`n=== Verifying ML Packages ===" -ForegroundColor Cyan
$packages = @("pandas", "numpy", "scikit-learn", "matplotlib", "seaborn", "scipy", "jupyter", "ipykernel")
$allInstalled = $true

foreach ($package in $packages) {
    $result = python -c "import $package; print('OK')" 2>&1
    if ($LASTEXITCODE -eq 0) {
        try {
            $version = python -c "import $package; print($package.__version__)" 2>&1
            Write-Host "[OK] $package $version" -ForegroundColor Green
        } catch {
            Write-Host "[OK] $package installed" -ForegroundColor Green
        }
    } else {
        Write-Host "[!] $package - NOT INSTALLED" -ForegroundColor Red
        $allInstalled = $false
    }
}

# Check data file
Write-Host "`n=== Data File Check ===" -ForegroundColor Cyan
if (Test-Path "data\data\raw\data_core.csv") {
    Write-Host "[OK] Data file found" -ForegroundColor Green
    $dataCheck = python -c "import pandas as pd; df = pd.read_csv('data/data/raw/data_core.csv'); print(f'{df.shape[0]} rows, {df.shape[1]} columns')" 2>&1
    Write-Host "Data shape: $dataCheck" -ForegroundColor White
} else {
    Write-Host "[!] Data file not found at data\data\raw\data_core.csv" -ForegroundColor Red
}

# Check Jupyter kernel
Write-Host "`n=== Jupyter Kernel Check ===" -ForegroundColor Cyan
$kernels = python -m jupyter kernelspec list 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Jupyter kernels available:" -ForegroundColor Green
    Write-Host $kernels -ForegroundColor White
} else {
    Write-Host "[!] Could not list kernels. You may need to register the kernel." -ForegroundColor Yellow
}

# Summary
Write-Host "`n=== Setup Summary ===" -ForegroundColor Cyan
if ($allInstalled) {
    Write-Host "[OK] All core ML packages are installed and working!" -ForegroundColor Green
    Write-Host "`nYour environment is ready for soil analysis ML work!" -ForegroundColor Green
    Write-Host "`nTo activate the environment in the future, run:" -ForegroundColor Yellow
    Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
    Write-Host "`nTo start Jupyter, run:" -ForegroundColor Yellow
    Write-Host "  jupyter notebook" -ForegroundColor White
    Write-Host "  or" -ForegroundColor White
    Write-Host "  jupyter lab" -ForegroundColor White
} else {
    Write-Host "[!] Some packages are missing. Installing requirements..." -ForegroundColor Yellow
    python -m pip install -r requirements.txt
}

Write-Host "`n=== Done ===" -ForegroundColor Green
