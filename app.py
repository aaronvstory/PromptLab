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

