import streamlit as st
import google.generativeai as genai
import time

# ✅ Streamlit Page Configuration for Hugging Face Spaces
st.set_page_config(page_title="PromptLab - AI Prompt Enhancer", layout="wide")
st.title("⚡ PromptLab - AI Prompt Enhancer")

# ✅ Retrieve the API key from Hugging Face secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Define Shinobi and Raikage Prompt Frameworks
SHINOBI_PROMPT = """You are an advanced prompt enhancer, specializing in creating structured, high-clarity prompts that optimize LLM performance.  
Your task is to refine a given prompt using the **Shinobi framework**, ensuring the following principles:  

✅ **Concise & High-Density Prompting** → Remove fluff, keeping instructions clear and actionable (~250 words max).  
✅ **Explicit Role Definition** → Assign a role to the AI for better contextual grounding.  
✅ **Step-by-Step Clarity** → Break the task into structured sections, avoiding ambiguity.  
✅ **Defined Output Format** → Specify the response format (JSON, CSV, list, structured text, etc.).  
✅ **Zero Conflicting Instructions** → Ensure clarity in constraints (e.g., avoid “simple yet comprehensive”).  
✅ **Optional: One-Shot Example** → Add a single example where relevant to guide the AI.  

### **Enhance the following prompt using Shinobi principles:**  
**Original Prompt:**  
{user_prompt}  

**Enhanced Shinobi Prompt:**  
"""

RAIKAGE_PROMPT = """You are an elite AI strategist, specializing in designing execution-focused prompts that maximize LLM efficiency.  
Your task is to refine a given prompt using the **Raikage framework**, ensuring the following principles:  

✅ **Precision & Depth** → Ensure expert-level guidance, reducing vagueness and ambiguity.  
✅ **Context & Execution Approach** → Include a structured methodology to solve the problem.  
✅ **Defined Output Format** → Specify exact structure (JSON, formatted text, markdown, tables, or code blocks).  
✅ **Edge Case Handling & Constraints** → Account for potential failures and model limitations.  
✅ **Optional: Few-Shot Prompting** → If beneficial, provide 1-2 high-quality examples for refinement.  
✅ **Complies with External Factors** → Adhere to best practices (e.g., ethical scraping, security policies).  

### **Enhance the following prompt using Raikage principles:**  
**Original Prompt:**  
{user_prompt}  

**Enhanced Raikage Prompt:**  
"""

# ✅ Streamlit UI Components
st.subheader("🛠️ Choose Your Enhancement Mode:")
mode = st.radio("Select a mode:", ["🌀 Shinobi", "⚡ Raikage"], horizontal=True)

user_prompt = st.text_area("✍️ Enter your prompt:", height=150)

# ✅ Button to Enhance Prompt
if st.button("🚀 Enhance Prompt"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a prompt before enhancing!")
    else:
        with st.spinner("⚡ Enhancing your prompt... Please wait"):
            time.sleep(1)  # 🔄 Smooth UI transition
            
            # Select the appropriate enhancement framework
            if mode == "🌀 Shinobi":
                full_prompt = SHINOBI_PROMPT.format(user_prompt=user_prompt)
            else:
                full_prompt = RAIKAGE_PROMPT.format(user_prompt=user_prompt)
            
            # ✅ Call Gemini API to Enhance the Prompt
            try:
                model = genai.GenerativeModel('gemini-2.0-flash')
                response = model.generate_content(full_prompt)
                
                # ✅ Display Enhanced Prompt
                st.subheader("✨ Enhanced Prompt:")
                st.text_area("", response.text, height=200)  # Read-only box
                
                # ✅ Copy to Clipboard Button
                st.code(response.text, language="markdown")

            except Exception as e:
                st.error(f"❌ API Error: {e}")
