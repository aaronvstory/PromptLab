@echo off
echo ========================================
echo    PromptLab - Starting Application
echo ========================================
echo.

cd /d "%~dp0"

if not exist "env\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    pause
    exit /b 1
)

if not exist ".streamlit\secrets.toml" (
    echo ERROR: secrets.toml not found!
    pause
    exit /b 1
)

echo Activating virtual environment...
call env\Scripts\activate.bat

echo Starting Streamlit (no auto-browser)...
echo.
echo Manually open: http://localhost:8501
echo Press Ctrl+C to stop
echo.

streamlit run app.py --server.headless true

pause
