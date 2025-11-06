# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PromptLab is a Streamlit-based web application that enhances user prompts using Google's Gemini AI (gemini-2.0-flash model). The application provides two enhancement modes:

- **Proficient Level**: General prompt enhancement with structured formatting and expert persona
- **Apex Level**: Advanced prompt engineering with comprehensive Context/Approach/Format framework

## Running the Application

### Quick Start
```bash
# Launch application (checks for env and secrets.toml)
run.bat
```

### Manual Start
```bash
# Activate virtual environment
env\Scripts\activate

# Run Streamlit application
streamlit run app.py

# Run on different port if 8501 is in use
streamlit run app.py --server.port 8502
```

Application opens at: http://localhost:8501

## Configuration

**Required**: Google Gemini API key must be configured in `.streamlit\secrets.toml`:
```toml
GEMINI_API_KEY = "your-api-key-here"
```

Get API key from: https://makersuite.google.com/app/apikey

## Project Structure

```
prompt-lab/
├── app.py                    # Main Streamlit application (99 lines)
├── requirements.txt          # Dependencies: streamlit, openai, google-generativeai
├── run.bat                   # Windows launcher with validation
├── .streamlit/
│   └── secrets.toml         # API key configuration (not in git)
└── env/                     # Python virtual environment
```

## Architecture

### Single-File Application (app.py)

**Main Components:**
- **Mode Selection**: Radio button for Proficient/Apex level (line 12)
- **API Configuration**: Retrieves API key from st.secrets (lines 14-18)
- **User Input**: Text area for prompt entry (line 21)
- **Template System**: Two prompt templates (lines 28-76)
  - `Proficient_TEMPLATE`: 7-step structured enhancement framework
  - `Apex_TEMPLATE`: Elite-level framework with Context/Approach/Format sections
- **Generation Logic**: Button triggers Gemini API call (lines 77-98)

**Known Bug in app.py (line 81-82):** ⚠️ CRITICAL
```python
if mode == "Shinobi":  # Should be "Proficient Level"
    prompt = Proficient_TEMPLATE.format(user_prompt=topic)
```
The mode comparison uses old names ("Shinobi"/"Raikage") instead of current radio button values ("Proficient Level"/"Apex Level"), causing Apex_TEMPLATE to always be used.

**Impact:** Proficient mode never works - all requests use Apex template regardless of user selection.

**Fix:**
```python
if mode == "Proficient Level":
    prompt = Proficient_TEMPLATE.format(user_prompt=topic)
```

### Error Handling
- API errors caught and displayed with st.error() (line 96)
- Empty prompt warning (line 98)
- run.bat validates env and secrets.toml exist before starting

## Dependencies

- **streamlit**: Web UI framework
- **google-generativeai**: Gemini API client (model: gemini-2.0-flash)
- **openai**: Listed but not actively used in current code

## Development Notes

- Virtual environment already configured in `env/` (488MB, 100+ packages)
- Secrets file `.streamlit/secrets.toml` excluded from git via .gitattributes
- No test suite present - **High priority to add**
- No build process required (Python/Streamlit)
- Application state is stateless; each generation is independent
- **Dead dependency:** `openai` package in requirements.txt but never imported - consider removing

## Common Issues & Solutions

### Issue: Mode Selection Not Working
**Symptom:** Both modes produce same results
**Cause:** Bug in mode comparison (line 81)
**Solution:** See bug fix above

### Issue: API Key Errors
**Symptom:** "Invalid API key" or secrets not found
**Solution:**
```bash
# Verify secrets.toml exists and has correct format
cat .streamlit/secrets.toml
# Should contain: GEMINI_API_KEY = "your-key-here"
```

### Issue: Slow Response Times
**Cause:** Synchronous API calls block UI
**Current:** No fix implemented (blocking by design)
**Future:** Consider implementing async API calls

## Performance Considerations

- **API Latency:** 2-5 seconds typical for Gemini responses
- **Rate Limits:** Free tier = 15 requests/minute
- **Caching:** None implemented - every request hits API
- **Concurrency:** Single-threaded, blocks during API call

## Testing Recommendations

Since no tests exist, when making changes:
1. Test both Proficient and Apex modes
2. Test with empty prompts (validation)
3. Test with very long prompts (5000+ chars)
4. Test API error scenarios (invalid key, network failure)
5. Verify secrets.toml loading

## Quick Reference

**Git Info:**
- Remote: https://huggingface.co/spaces/hruday96/prompt-lab
- Recent commits: All labeled "Update app.py"

**Key Dependencies:**
- streamlit (1.43.0) - Web framework
- google-generativeai (0.8.5) - AI client
- Python 3.13.5 runtime

**For comprehensive architecture analysis, see:** `codebase_analysis.md`
