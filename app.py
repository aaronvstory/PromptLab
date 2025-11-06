import streamlit as st
import google.generativeai as genai

# Model configuration
GEMINI_MODEL = "gemini-2.5-pro"

st.set_page_config(page_title="PromptLab", layout="wide")

# Streamlit app layout
st.title('PromptLab')

# Display current model
st.info(f"🤖 Current AI Model: **{GEMINI_MODEL}**")

# Retrieve the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure the Google Generative AI API with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# ---------------- Templates ----------------
Proficient_TEMPLATE = """
Analyze the following user prompt and transform it into an enhanced, structured prompt following these steps:

1. Determine the primary subject area and required expertise level
2. Formulate an expert persona introduction ("You are an expert in [subject]")
3. Define the user-AI interaction pattern
4. Create appropriate response structure:
   a. For simple topics: Use general formatting guidelines
   b. For complex topics: Create numbered sections with descriptive headers
   c. Adjust detail level based on topic complexity
5. Specify content requirements (examples, definitions, code samples, etc.)
6. Include quality guidelines for clarity, conciseness, and accessibility
7. Preserve the original user prompt at the end marked with "Input:"

Enhance the following prompt using this **structured, Proficient-level framework:**

**Original Prompt:**
{user_prompt}

**Enhanced Prompt:**
(Apply the Primer framework to generate the improved version)
"""

Apex_TEMPLATE = """
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

# 3) Quick Refiner (general purpose)
QuickRefiner_TEMPLATE = """
You are a helpful assistant. Tighten this prompt so it's clear and specific.

Do:
- Keep it brief and actionable.
- Add only missing essentials: goal, key constraints, output format.
- Avoid long preambles or personas.
- Preserve the user's intent and domain terms.

Return:
1) Refined Prompt (single block, <= {word_limit} words)
2) Notes (bulleted: what you clarified or cut)
3) Risks (any gaps to watch)

Input:
{user_prompt}
"""

# 4) Code Task Sharpener (coding)
CodeSharpener_TEMPLATE = """
You are a coding copilot. Rewrite the request into a compact build brief.

Include only if present or critical:
- Goal: what to build or fix.
- Context: stack, file paths, interfaces, versions.
- Constraints: performance, security, style, tests, time.
- Output: exact deliverable (e.g., "diff for file X", "function with signature ...", "pytest tests").
- Example I/O: at most 1 tiny example only if it reduces ambiguity.

Return:
Refined Dev Prompt (<= {word_limit} words, no persona, no steps unless required)
Then a one-liner command or file list if relevant.

User request:
{user_prompt}
"""

# 5) Spec-to-Answer Mini Brief (concise structure)
MiniBrief_TEMPLATE = """
Rewrite the prompt into a mini brief the model can act on immediately.

Sections (each 1–2 lines max):
- Goal
- Must-include context (only what's required)
- Output format (schema, bullets, or code block)
- Quality checks (2–3 crisp criteria)

Return the brief only, no extra text. Limit to <= {word_limit} words.

Input:
{user_prompt}
"""

# ---------------- UI ----------------
mode = st.selectbox(
    "Choose enhancer mode",
    ["Proficient Level", "Apex Level", "Quick Refiner", "Code Task Sharpener", "Mini Brief"],
    index=0
)

# Add-on toggles
st.caption("Optional add-ons")
col1, col2, col3 = st.columns(3)
with col1:
    add_example = st.checkbox("Add one tiny example if it truly removes ambiguity")
with col2:
    token_guard = st.checkbox("Apply token guard (tight word limit)", value=True)
with col3:
    cite_or_unknown = st.checkbox("Ask for citations or let the model say 'unknown' for research tasks")

# Word limit control (used when token_guard is on)
default_limit = 120 if mode == "Quick Refiner" else 150
word_limit = st.number_input("Word limit", min_value=60, max_value=300, value=default_limit, step=10)

# Input field for the prompt
topic = st.text_area('Enter your prompt:')

# Display selected mode
st.write(f"You selected: {mode}")

# Show template preview for the selected mode
with st.expander("📋 View Selected Template"):
    if mode == "Proficient Level":
        st.code(Proficient_TEMPLATE.replace("{user_prompt}", "[YOUR PROMPT WILL BE INSERTED HERE]"), language="text")
    elif mode == "Apex Level":
        st.code(Apex_TEMPLATE.replace("{user_prompt}", "[YOUR PROMPT WILL BE INSERTED HERE]"), language="text")
    elif mode == "Quick Refiner":
        st.code(QuickRefiner_TEMPLATE.format(user_prompt="[YOUR PROMPT WILL BE INSERTED HERE]", word_limit=word_limit), language="text")
    elif mode == "Code Task Sharpener":
        st.code(CodeSharpener_TEMPLATE.format(user_prompt="[YOUR PROMPT WILL BE INSERTED HERE]", word_limit=word_limit), language="text")
    else:
        st.code(MiniBrief_TEMPLATE.format(user_prompt="[YOUR PROMPT WILL BE INSERTED HERE]", word_limit=word_limit), language="text")

# ---------------- Prompt assembly helpers ----------------
def apply_addons(template_text: str, supports_limit: bool) -> str:
    """Append compact add-on instructions only when toggles are on."""
    add_lines = []
    if add_example:
        add_lines.append(
            "If a tiny example would remove ambiguity, include exactly one minimal example; otherwise do not add examples."
        )
    if token_guard and supports_limit:
        add_lines.append(f"Hard cap total length at <= {word_limit} words for the main refined prompt.")
    if cite_or_unknown:
        add_lines.append(
            "For factual claims, cite sources briefly when possible. If unsure, say you don't know."
        )
    if add_lines:
        template_text += """

Add-ons:
- """ + "\n- ".join(add_lines)
    return template_text

# ---------------- Generate ----------------
if st.button("Generate Enhanced Prompt"):
    if topic.strip():
        with st.spinner("Enhancing your prompt..."):
            # Choose base template
            if mode == "Proficient Level":
                base = Proficient_TEMPLATE.format(user_prompt=topic)
                supports_limit = False
            elif mode == "Apex Level":
                base = Apex_TEMPLATE.format(user_prompt=topic)
                supports_limit = False
            elif mode == "Quick Refiner":
                base = QuickRefiner_TEMPLATE.format(user_prompt=topic, word_limit=word_limit)
                supports_limit = True
            elif mode == "Code Task Sharpener":
                base = CodeSharpener_TEMPLATE.format(user_prompt=topic, word_limit=word_limit)
                supports_limit = True
            else:
                base = MiniBrief_TEMPLATE.format(user_prompt=topic, word_limit=word_limit)
                supports_limit = True

            prompt = apply_addons(base, supports_limit)

            # Call Gemini
            try:
                model = genai.GenerativeModel(GEMINI_MODEL)
                response = model.generate_content(prompt)
                enhanced_prompt = response.text or ""
                st.subheader("🔹 Enhanced Prompt:")
                st.write(enhanced_prompt)
            except Exception as e:
                st.error(f"❌ Error generating enhanced prompt: {e}")
    else:
        st.warning("⚠️ Please enter a prompt before generating.")
