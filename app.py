import streamlit as st
import google.generativeai as genai

# Configure API Key
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# Streamlit App Layout
st.title('PromptLab')

# Mode Selection (Shinobi & Raikage)
mode = st.radio("Select a mode:", ["🌀 Shinobi", "⚡ Raikage"], horizontal=True)

# User Input
user_prompt = st.text_area('Enter your prompt:')

# Function to Generate Enhanced Prompt
def generate_enhanced_prompt(user_prompt, mode):
    if mode == "🌀 Shinobi":
        system_prompt = "You are an expert in structured prompt design. Refine the following prompt for clarity, conciseness, and structured output."
    elif mode == "⚡ Raikage":
        system_prompt = "You are a world-class AI strategist specializing in execution-focused prompts. Transform the following prompt for high-impact, expert-level results."
    
    # Generate response using Gemini API
    response = genai.generate_content(system_prompt + "\n\n" + user_prompt)
    return response

# Process User Input
if st.button("Generate Enhanced Prompt"):
    if user_prompt.strip():
        with st.spinner("Enhancing prompt..."):
            enhanced_prompt = generate_enhanced_prompt(user_prompt, mode)
            st.subheader("Enhanced Prompt:")
            st.code(enhanced_prompt, language='markdown')
    else:
        st.warning("Please enter a prompt before generating.")
