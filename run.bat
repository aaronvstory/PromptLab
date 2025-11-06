@echo off
REM Windows batch script to run PromptLab Streamlit application

echo ========================================
echo    PromptLab - Starting Application
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "env\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first.
    pause
    exit /b 1
)

REM Check if secrets file exists
if not exist ".streamlit\secrets.toml" (
    echo ERROR: secrets.toml not found!
    echo Please configure your Google Gemini API key in .streamlit\secrets.toml
    pause
    exit /b 1
)

REM Activate virtual environment and run Streamlit
echo Activating virtual environment...
call env\Scripts\activate.bat

REM Extract and display current model from app.py
for /f "tokens=2 delims==" %%i in ('findstr /c:"GEMINI_MODEL = " app.py') do set MODEL_NAME=%%i
set MODEL_NAME=%MODEL_NAME:"=%
set MODEL_NAME=%MODEL_NAME: =%
echo Current AI Model: %MODEL_NAME%
echo.

echo Starting Streamlit application...
echo.
echo The application will open in your default browser.
echo Press Ctrl+C to stop the server.
echo.

streamlit run app.py

pause
