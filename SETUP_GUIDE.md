# PromptLab - Local Setup Guide

## Overview
PromptLab is a Streamlit application that enhances your prompts using Google's Gemini AI. It offers two enhancement modes:
- **Proficient Level**: General prompt enhancement with structured formatting
- **Apex Level**: Elite-level prompt enhancement with advanced frameworks

## Prerequisites
- Python 3.8 or higher
- Google Gemini API key (free from Google AI Studio)

## Setup Instructions

### 1. Get Your Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

### 2. Configure API Key
Edit the file `.streamlit\secrets.toml` and replace `YOUR_GEMINI_API_KEY_HERE` with your actual API key:

```toml
GEMINI_API_KEY = "your-actual-api-key-here"
```

**Important**: Keep this file secure and never share your API key publicly!

### 3. Run the Application

#### Option A: Use the Batch Script (Easiest)
Double-click `run.bat` or run from command line:
```bash
run.bat
```

#### Option B: Manual Start
```bash
# Activate virtual environment
env\Scripts\activate

# Run Streamlit
streamlit run app.py
```

### 4. Access the Application
The application will automatically open in your default browser at:
```
http://localhost:8501
```

If it doesn't open automatically, manually navigate to that URL.

## Using PromptLab

1. **Select a Mode**: Choose between "Proficient Level" or "Apex Level"
2. **Enter Your Prompt**: Type your original prompt in the text area
3. **Generate**: Click "Generate Enhanced Prompt" button
4. **Review**: The enhanced prompt will appear below

### Mode Descriptions

**Proficient Level**
- General-purpose prompt enhancement
- Structures prompts with clear sections
- Adds expert persona and context
- Best for everyday tasks

**Apex Level**
- Advanced prompt engineering
- Elite-level structuring with Context/Approach/Format
- Best practices and edge case handling
- Ideal for complex, professional tasks

## Troubleshooting

### "ERROR: Virtual environment not found"
Run the setup again:
```bash
python -m venv env
env\Scripts\pip install -r requirements.txt
```

### "ERROR: secrets.toml not found"
Make sure you created the `.streamlit\secrets.toml` file with your API key.

### API Key Errors
- Verify your API key is correct in `.streamlit\secrets.toml`
- Ensure you have API quota remaining in Google AI Studio
- Check your internet connection

### Port Already in Use
If port 8501 is already in use, specify a different port:
```bash
streamlit run app.py --server.port 8502
```

## Project Structure
```
prompt-lab/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── run.bat                   # Windows startup script
├── SETUP_GUIDE.md           # This file
├── .streamlit/
│   └── secrets.toml         # API key configuration (not in git)
└── env/                     # Python virtual environment (not in git)
```

## Security Notes
- Never commit `.streamlit/secrets.toml` to version control
- The `.gitattributes` file already excludes secrets files
- Keep your API key private and rotate it if exposed

## Updating Dependencies
To update all dependencies to the latest versions:
```bash
env\Scripts\activate
pip install --upgrade -r requirements.txt
```

## Deactivating Virtual Environment
When you're done, deactivate the virtual environment:
```bash
deactivate
```

## Additional Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Original Hugging Face Space](https://huggingface.co/spaces/hruday96/prompt-lab)

## Support
For issues with the application itself, check the original repository or Hugging Face Space.
