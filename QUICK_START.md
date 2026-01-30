# Quick Start Guide

## Activating the Environment

You have several options to activate the virtual environment:

### Option 1: Direct Activation (Recommended)
```powershell
.\venv\Scripts\Activate.ps1
```

### Option 2: Using the Activation Script
```powershell
.\activate_env.ps1
```

If you get an execution policy error, try:
```powershell
powershell -ExecutionPolicy Bypass -File .\activate_env.ps1
```

### Option 3: Manual Activation
```powershell
cd "c:\Users\tigra\Soil Analysis"
.\venv\Scripts\Activate.ps1
```

## After Activation

Once activated, you'll see `(venv)` in your prompt. Then you can:

1. **Start Jupyter Notebook:**
   ```powershell
   jupyter notebook
   ```

2. **Start JupyterLab:**
   ```powershell
   jupyter lab
   ```

3. **Run Python scripts:**
   ```powershell
   python your_script.py
   ```

4. **Install additional packages:**
   ```powershell
   pip install package_name
   ```

## Troubleshooting

### "Script not recognized" Error
If PowerShell says the script is not recognized:
- Make sure you're in the correct directory: `cd "c:\Users\tigra\Soil Analysis"`
- Try using the full path: `& "c:\Users\tigra\Soil Analysis\venv\Scripts\Activate.ps1"`

### Execution Policy Error
If you get an execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

### Alternative: Use Command Prompt
If PowerShell continues to have issues, you can use Command Prompt (cmd):
```cmd
cd "c:\Users\tigra\Soil Analysis"
venv\Scripts\activate.bat
```

## Verify Installation

To verify everything is working:
```powershell
python -c "import pandas, numpy, sklearn; print('All packages installed!')"
```
