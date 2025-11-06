# Fix: Python 3.13.5 Incompatibility

## Problem
Python 3.13.5 causes Streamlit to hang on import. Need Python 3.11.

## Solution

### Step 1: Install Python 3.11
```bash
scoop install python311
# OR download from: https://www.python.org/downloads/release/python-3119/
```

### Step 2: Recreate Virtual Environment
```bash
cd C:\claude\PromptLab\prompt-lab
rm -rf env
python3.11 -m venv env
```

### Step 3: Reinstall Dependencies
```bash
.\env\Scripts\activate
pip install -r requirements.txt
```

### Step 4: Test
```bash
.\env\Scripts\python.exe -c "import streamlit; print(streamlit.__version__)"
```

### Step 5: Launch
```bash
run.bat
```

## Quick Alternative: Use Online Version
Until Python 3.11 is installed, you can use the Hugging Face hosted version:
https://huggingface.co/spaces/hruday96/prompt-lab
