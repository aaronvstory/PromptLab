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
You are an advanced prompt enhancer designed to refine and expand prompts for clarity, structure, and engagement.  
Your task is to take a given prompt and improve it using the **Enhanced Primer framework**, ensuring the following:  

✅ **Assign a Role** → Clearly define the user's role to set context.  
✅ **Define a Clear Objective** → Clarify the task and expected outcome.  
✅ **Break Down Content** → Structure the response into key sections with subtopics.  
✅ **Enhance Style & Clarity** → Ensure the response is actionable, practical, and easy to follow.  
✅ **Adapt to Audience Level** → Adjust depth and complexity for different users.  
✅ **Suggest Examples (If Needed)** → Add relevant real-world examples for better understanding.  
✅ **Control Output Format** → Ensure the response aligns with the expected format (list, guide, paragraph, etc.).  

**Enhance the following prompt using this structured approach:**  

**Original Prompt:**  
{user_prompt}  

**Enhanced Prompt:**  
(Apply the Enhanced Primer framework to generate the improved version)      
"""

RAIKAGE_TEMPLATE = """
You are an elite-level [role] with deep expertise in [subject].  
Your task is to develop a structured, high-quality response following these key elements:  

## **Context**  
[Provide background information related to the task to frame the problem.]  

## **Approach**  
[Define a **step-by-step** breakdown of how to achieve the goal, focusing on methodology and best practices.]  

## **Response Format**  
[Specify the expected output structure, ensuring clarity and completeness.]  

## **Instructions**  
- [Ensure high-quality standards, best practices, and possible constraints.]  
- [Emphasize documentation, flexibility, and potential edge cases.]  

Enhance the following prompt using this **structured, expert-level framework:**  

**Original Prompt:**  
{user_prompt}  

**Enhanced Prompt:**  
(Apply the Mastermind framework to generate the improved version)    
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
                st.code(enhanced_prompt, language="markdown")
            except Exception as e:
                st.error(f"❌ Error generating enhanced prompt: {e}")
    else:
        st.warning("⚠️ Please enter a prompt before generating.")
