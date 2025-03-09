import streamlit as st
import google.generativeai as genai

# 🔑 Load API Key from Streamlit Secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 🎨 Streamlit UI Setup
st.title("⚡ PromptLab – AI-Powered Prompt Enhancer")
st.write("Enhance your prompts with **Shinobi** (Structured) or **Raikage** (Execution-Focused)")

# 🎭 Mode Selection
mode = st.radio("Select Mode:", ["🌀 Shinobi", "⚡ Raikage"], horizontal=True)

# ✍️ User Input for Prompt
user_prompt = st.text_area("Enter your prompt:")

# 🚀 Generate Enhanced Prompt
if st.button("Enhance Prompt"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a prompt before enhancing.")
    else:
        with st.spinner("Enhancing your prompt... ⚡"):
            # 🛠️ Apply Shinobi or Raikage Framework
            if mode == "🌀 Shinobi":
                structured_prompt = f"""
                You are an advanced prompt enhancer, specializing in creating structured, high-clarity prompts that optimize LLM performance.
                Your task is to refine a given prompt using the **Shinobi framework**, ensuring:
                
                ✅ **Concise & High-Density Prompting** → Remove fluff, keeping instructions clear and actionable.
                ✅ **Explicit Role Definition** → Assign a role to the AI for better contextual grounding.
                ✅ **Step-by-Step Clarity** → Break the task into structured sections.
                ✅ **Defined Output Format** → Specify the response format.
                
                ### **Enhance the following prompt using Shinobi principles:**
                
                **Original Prompt:**  
                {user_prompt}
                
                **Enhanced Shinobi Prompt:**  
                """
            else:
                structured_prompt = f"""
                You are an elite AI strategist, specializing in designing execution-focused prompts that maximize LLM efficiency.
                Your task is to refine a given prompt using the **Raikage framework**, ensuring:
                
                ✅ **Precision & Depth** → Ensure expert-level guidance, reducing vagueness.
                ✅ **Context & Execution Approach** → Include a structured methodology.
                ✅ **Defined Output Format** → Specify exact structure (JSON, markdown, tables, etc.).
                ✅ **Edge Case Handling & Constraints** → Account for potential failures.
                
                ### **Enhance the following prompt using Raikage principles:**
                
                **Original Prompt:**  
                {user_prompt}
                
                **Enhanced Raikage Prompt:**  
                """

            # 🧠 Call Gemini API
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(structured_prompt)

            # 📝 Display Output
            enhanced_prompt = response.text.strip()
            st.subheader("🔹 Enhanced Prompt:")
            st.code(enhanced_prompt, language="markdown")

            # 📋 Copy Button
            st.button("📋 Copy to Clipboard", on_click=lambda: st.session_state.update({"copied_text": enhanced_prompt}))


