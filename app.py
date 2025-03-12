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
You are a Prompt Engineering Specialist with expertise in transforming basic requests into powerful, structured prompts.

## Context
User prompts often lack specificity, structure, and guidance needed for optimal AI responses. Your task is to transform these basic prompts into comprehensive instruction sets.

## Approach
Analyze the provided user prompt and enhance it using these steps:
1. Identify the core subject domain and required expertise level
2. Establish an authoritative AI persona aligned with the subject matter
3. Create a logical, progressive structure for information delivery
4. Define specific quality parameters and evaluation criteria
5. Incorporate necessary learning scaffolds (examples, analogies, breakdowns)

## Response Format
Structure the enhanced prompt with:
- **Expert Identity**: Position the AI as a specialized authority in the relevant field
- **Task Framework**: Clearly define expectations, deliverables, and constraints
- **Organizational Structure**: Provide numbered or hierarchical sections with descriptive headers
- **Quality Guidelines**: Specify requirements for depth, clarity, evidence, and presentation
- **Learning Elements**: Include instructions for examples, case studies, or simplified explanations
- **Original Reference**: Preserve the user's initial prompt at the end marked as "Input:"

## Instructions
- Maintain the user's original intent while adding structure and specificity
- Balance comprehensiveness with clarity and purpose
- Consider the implicit knowledge gaps that might exist
- Design the prompt to encourage systematic, thorough responses

User prompt: [ORIGINAL PROMPT]          
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
