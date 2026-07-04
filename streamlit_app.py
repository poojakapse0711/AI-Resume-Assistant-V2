import streamlit as st

from src.backend import initialize_rag
from src.file_manager import save_uploaded_pdf
from src.resume_features import (
    generate_summary,
    extract_skills,
    interview_questions,
    improvement_suggestions,
)
from src.ats import analyze_resume


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="🤖",
    layout="wide"
)

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("🤖 AI Resume Assistant")

    st.markdown("---")

    st.markdown("### 📌 Features")

    st.markdown("""
- 💬 Chat with Resume
- 📋 Resume Summary
- 🛠 Skill Extraction
- 🎤 Interview Questions
- 📈 ATS Resume Analysis
""")

    st.markdown("---")

    st.info(
        """
Built using

- Google Gemini
- LangChain
- FAISS
- Streamlit
"""
    )

    st.markdown("---")

    st.caption("Developed by Pooja Kapse")

# ==========================================================
# Main Header
# ==========================================================

st.title("🤖 AI Resume Assistant")

st.caption(
    "Upload your resume and interact with it using "
    "Google Gemini + LangChain + FAISS."
)

st.divider()

# ==========================================================
# Session State
# ==========================================================

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================================
# Upload Resume
# ==========================================================

st.subheader("📄 Upload Resume")

uploaded_file = st.file_uploader(
    "Choose a PDF Resume",
    type=["pdf"],
    help="Upload your resume in PDF format."
)

if uploaded_file is not None and st.session_state.rag_chain is None:

    pdf_path = save_uploaded_pdf(uploaded_file)

    with st.spinner("Creating AI Knowledge Base..."):

        st.session_state.rag_chain = initialize_rag(pdf_path)

    st.success(
        "✅ Resume uploaded successfully. "
        "You can now chat with your resume."
    )

# ==========================================================
# Main Dashboard
# ==========================================================

if st.session_state.rag_chain is not None:

    (
        chat_tab,
        summary_tab,
        skills_tab,
        interview_tab,
        suggestion_tab,
        ats_tab,
    ) = st.tabs(
        [
            "💬 Chat",
            "📋 Summary",
            "🛠 Skills",
            "🎤 Interview",
            "📈 Suggestions",
            "📊 ATS Analysis",
        ]
    )

    # ======================================================
    # CHAT
    # ======================================================

    with chat_tab:

        for message in st.session_state.messages:

            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        prompt = st.chat_input(
            "Ask anything about your resume..."
        )

        if prompt:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": prompt
                }
            )

            with st.chat_message("user"):
                st.markdown(prompt)

            with st.spinner("Thinking..."):

                response = st.session_state.rag_chain.invoke(
                    {
                        "input": prompt
                    }
                )

                answer = response["answer"]

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            with st.chat_message("assistant"):
                st.markdown(answer)

    # ======================================================
    # SUMMARY
    # ======================================================

    with summary_tab:

        st.subheader("Resume Summary")

        if st.button("Generate Summary"):

            with st.spinner("Generating Summary..."):

                summary = generate_summary(
                    st.session_state.rag_chain
                )

            st.markdown(summary)

    # ======================================================
    # SKILLS
    # ======================================================

    with skills_tab:

        st.subheader("Technical Skills")

        if st.button("Extract Skills"):

            with st.spinner("Extracting Skills..."):

                skills = extract_skills(
                    st.session_state.rag_chain
                )

            st.markdown(skills)

    # ======================================================
    # INTERVIEW
    # ======================================================

    with interview_tab:

        st.subheader("Interview Questions")

        if st.button("Generate Interview Questions"):

            with st.spinner("Generating Questions..."):

                questions = interview_questions(
                    st.session_state.rag_chain
                )

            st.markdown(questions)

    # ======================================================
    # SUGGESTIONS
    # ======================================================

    with suggestion_tab:

        st.subheader("Resume Improvement Suggestions")

        if st.button("Generate Suggestions"):

            with st.spinner("Analyzing Resume..."):

                suggestions = improvement_suggestions(
                    st.session_state.rag_chain
                )

            st.markdown(suggestions)

    # ======================================================
    # ATS
    # ======================================================

    with ats_tab:

        st.subheader("ATS Resume Analyzer")

        job_description = st.text_area(
            "Paste Job Description",
            height=250
        )

        if st.button("Analyze Resume"):

            if job_description.strip() == "":

                st.warning(
                    "Please paste a Job Description."
                )

            else:

                with st.spinner("Analyzing Resume..."):

                    report = analyze_resume(
                        st.session_state.rag_chain,
                        job_description
                    )

                st.markdown(report)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "Version 1.0 | AI Resume Assistant | Built with ❤️ using Streamlit"
)