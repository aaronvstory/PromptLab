import streamlit as st
import google.generativeai as genai

# Streamlit app layout
st.title('PromptLab')

# Create two columns for the Shinobi and Raikage buttons
col1, col2 = st.columns(2)

mode = st.radio("Choose a mode:", ["Shinobi", "Raikage"], horizontal=True)

# Retrieve the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure the Google Generative AI API with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Input field for the blog topic
topic = st.text_area('Enter your prompt:')

# Display selected mode
st.write(f"You selected: {mode}")


# Shinobi and Raikage templates
SHINOBI_TEMPLATE = """
You are an advanced prompt enhancer, specializing in creating structured, high-clarity prompts that optimize LLM performance.  
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

RAIKAGE_TEMPLATE = """
You are an elite AI strategist, specializing in designing execution-focused prompts that maximize LLM efficiency.  
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
if st.button("Generate Enhanced Prompt"):
    if topic.strip():
        with st.spinner("Enhancing your prompt..."):
            # Choose the template based on the selected mode
            if mode == "Shinobi":
                prompt = SHINOBI_TEMPLATE.format(user_prompt=topic)
            else:
                prompt = RAIKAGE_TEMPLATE.format(user_prompt=topic)

            # Initialize the generative model
            model = genai.GenerativeModel('gemini-2.0-flash')

            # Generate enhanced prompt
            try:
                response = model.generate_content(prompt)
                enhanced_prompt = response.text  # Extract the response text
                st.subheader("🔹 Enhanced Prompt:")
                st.subheader(enhanced_prompt, language="markdown")
            except Exception as e:
                st.error(f"❌ Error generating enhanced prompt: {e}")
    else:
        st.warning("⚠️ Please enter a prompt before generating.")
