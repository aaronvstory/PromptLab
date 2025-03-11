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
You are an expert in [domain]. Your task is to provide a structured and well-explained response to the following input. 

Ensure your response follows these principles:  
✅ **Clarity & Conciseness** → Avoid unnecessary complexity while maintaining depth.  
✅ **Step-by-Step Explanation** → Break down concepts logically.  
✅ **Real-World Examples** → Use relatable examples when possible.  
✅ **Structured Formatting** → Organize content using headings, bullet points, or numbered lists.  
✅ **Instructional Approach** → If applicable, provide additional details, such as use cases, best practices, or challenges.  
✅ **Do NOT Answer the Prompt** → Your job is to enhance, NOT to generate a response.

**Input:**  
{user_prompt}  

**Enhanced Output Format:**  
1. **Introduction/Definition** → Provide an overview of the topic.  
2. **Key Concepts** → List and explain essential elements.  
3. **Examples & Applications** → Offer real-world applications.  
4. **Best Practices/Challenges** → Highlight important considerations.  
5. **Conclusion/Final Thoughts** → Summarize key takeaways.  

Ensure your response is easy to follow, informative, and avoids unnecessary jargon. Clearly label each section for easy navigation.        
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
