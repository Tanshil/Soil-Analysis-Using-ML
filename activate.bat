@echo off
REM Quick activation for Windows CMD
call venv\Scripts\activate.bat
echo Soil Analysis environment activated (venv)
echo Quick commands:
echo   jupyter notebook
echo   jupyter lab
echo   python src\run_training.py
echo   deactivate  # to exit
pause

