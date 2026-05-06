# Quick Start Guide (Cross-Platform)

## Setup (First Time)
**Linux/Mac/Git Bash**: `./setup.sh`  
**Windows CMD**: `setup.bat`

## Activation
**Linux/Mac/Git Bash:**
```
source activate.sh
# or source venv/bin/activate
```

**Windows CMD:**
```
activate.bat
# or venv\\Scripts\\activate.bat
```

**Windows PowerShell:**
```
venv\\Scripts\\Activate.ps1
```

*Look for `(venv)` in prompt.*

## Usage
```
jupyter notebook     # or jupyter lab
python src/run_training.py
pip install extra_pkg  # if needed
deactivate           # exit venv
```

## Verify
```
python -c "import pandas, sklearn; print('Ready for soil analysis!')"
```

## Troubleshooting
- **No venv?** Delete `venv/`, rerun setup.
- **Wrong dir?** `cd` to project root.
- **Windows policy?** Use CMD/Git Bash.
- **Packages missing?** Rerun setup.

Project now runs on **Windows, Linux, Mac** without changes!
