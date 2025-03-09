import streamlit as st
import google.generativeai as genai

# Configure API Key
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# Select Gemini Model
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit App Layout
st.title('PromptLab')

# Mode Selection (Shinobi & Raikage)
mode = st.radio("Select a mode:", ["🌀 Shinobi", "⚡ Raikage"], horizontal=True)

# User Input
st.subheader("Enter Your Prompt:")
user_prompt = st.text_area('Enter your prompt:')

# Function to Generate Enhanced Prompt
def get_gemini_response(prompt):
    try:
        response = gemini_model.generate_content(prompt)
        return response.text if response else "Error: No response received."
    except Exception as e:
        return f"❌ Gemini error: {e}"

# Function to Format Prompt Based on Mode
def generate_enhanced_prompt(user_prompt, mode):
    if mode == "🌀 Shinobi":
        system_prompt = "You are an expert in structured prompt design. Refine the following prompt for clarity, conciseness, and structured output."
    elif mode == "⚡ Raikage":
        system_prompt = "You are a world-class AI strategist specializing in execution-focused prompts. Transform the following prompt for high-impact, expert-level results."
    
    # Generate response using Gemini API
    return get_gemini_response(system_prompt + "\n\n" + user_prompt)

# Button to Submit the Prompt
if st.button("Generate Enhanced Prompt"):
    if user_prompt.strip():
        try:
            with st.spinner("Enhancing prompt..."):
                enhanced_prompt = generate_enhanced_prompt(user_prompt, mode)
                st.subheader("Enhanced Prompt:")
                st.write(enhanced_prompt)  # Displaying the text from the response
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt before generating.")

# Footer
st.markdown("Built with 🧠 by Hruday & Google Gemini")
