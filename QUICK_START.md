# PromptLab - Quick Start Guide

## ✅ Setup Complete!

Your PromptLab application is now ready to run locally on Windows.

## 🚀 How to Run

### Step 1: Get Your Google Gemini API Key
1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Create a new API key (it's free!)
4. Copy the key

### Step 2: Configure Your API Key
1. Open the file: `.streamlit\secrets.toml`
2. Replace `YOUR_GEMINI_API_KEY_HERE` with your actual API key
3. Save the file

### Step 3: Launch the Application
Simply double-click: **`run.bat`**

Or from command line:
```bash
cd C:\claude\PromptLab\prompt-lab
run.bat
```

The application will automatically open in your browser at: http://localhost:8501

## 📁 What's Included

```
prompt-lab/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies (already installed)
├── run.bat                   # One-click startup script
├── SETUP_GUIDE.md           # Detailed setup instructions
├── QUICK_START.md           # This file
├── .streamlit/
│   └── secrets.toml         # API key configuration (EDIT THIS!)
└── env/                     # Python virtual environment (ready to go)
```

## 🎯 Using PromptLab

1. **Choose Mode**: Proficient Level or Apex Level
2. **Enter Prompt**: Type your original prompt
3. **Generate**: Click the button
4. **Copy Result**: Use your enhanced prompt!

### Mode Comparison

| Feature | Proficient Level | Apex Level |
|---------|-----------------|------------|
| Structure | Simple sections | Advanced framework |
| Detail | Moderate | Comprehensive |
| Use Case | General tasks | Complex projects |
| Persona | Standard expert | Elite-level specialist |

## 🔧 What Was Done

✅ Cloned repository from Hugging Face
✅ Created Python virtual environment
✅ Installed all dependencies (Streamlit, Google Gemini AI, OpenAI)
✅ Created `.streamlit/secrets.toml` for API key
✅ Created Windows batch script for easy startup
✅ Generated comprehensive documentation

## ⚠️ Important Notes

1. **API Key Required**: The app won't work without a Google Gemini API key
2. **Free Tier**: Google Gemini has a generous free tier for testing
3. **Internet Required**: The app needs internet to connect to Gemini API
4. **Keep Secrets Safe**: Never share your `.streamlit/secrets.toml` file

## 🆘 Troubleshooting

### "ERROR: secrets.toml not found"
→ Make sure you have the API key file at: `.streamlit\secrets.toml`

### "Invalid API Key" error
→ Double-check your API key in the secrets.toml file
→ Ensure there are no extra spaces or quotes

### Port already in use
→ Close other applications using port 8501
→ Or run: `streamlit run app.py --server.port 8502`

### Application won't start
→ Make sure Python is installed
→ Run: `env\Scripts\activate` then `streamlit run app.py`

## 📚 Additional Resources

- **Full Setup Guide**: See `SETUP_GUIDE.md` for detailed instructions
- **Streamlit Docs**: https://docs.streamlit.io/
- **Gemini API**: https://ai.google.dev/docs
- **Original Space**: https://huggingface.co/spaces/hruday96/prompt-lab

## 🎉 Next Steps

1. Get your API key from Google AI Studio
2. Edit `.streamlit\secrets.toml` with your key
3. Run `run.bat`
4. Start enhancing your prompts!

---

**Setup completed**: October 9, 2025
**Location**: C:\claude\PromptLab\prompt-lab
**Status**: Ready to run (API key needed)
