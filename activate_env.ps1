# Quick activation script for the virtual environment
# Usage: .\activate_env.ps1

Write-Host "Activating Soil Analysis environment..." -ForegroundColor Cyan
& ".\venv\Scripts\Activate.ps1"
Write-Host "Environment activated! You can now run Python scripts and Jupyter notebooks." -ForegroundColor Green
Write-Host "`nQuick commands:" -ForegroundColor Yellow
Write-Host "  jupyter notebook  - Start Jupyter Notebook" -ForegroundColor White
Write-Host "  jupyter lab      - Start JupyterLab" -ForegroundColor White
Write-Host "  python -m pip list - List installed packages" -ForegroundColor White
