import os
import streamlit as st

from src.backend import initialize_rag
from src.resume_features import (
    generate_summary,
    extract_skills,
    interview_questions,
    improvement_suggestions,
)

st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Assistant")

st.markdown("---")

# ---------------- Session State ---------------- #

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Upload ---------------- #

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None and st.session_state.rag_chain is None:

    os.makedirs("data", exist_ok=True)

    pdf_path = os.path.join(
        "data",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Creating Knowledge Base..."):

        st.session_state.rag_chain = initialize_rag(pdf_path)

    st.success("✅ Resume Uploaded Successfully!")

# ---------------- Main UI ---------------- #

if st.session_state.rag_chain is not None:

    chat_tab, summary_tab, skills_tab, interview_tab, suggestion_tab = st.tabs(
        [
            "💬 Chat",
            "📋 Summary",
            "🛠 Skills",
            "🎤 Interview",
            "📈 Suggestions",
        ]
    )

    # ---------------- CHAT ---------------- #

    with chat_tab:

        for msg in st.session_state.messages:

            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

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

    # ---------------- SUMMARY ---------------- #

    with summary_tab:

        st.subheader("Resume Summary")

        if st.button("Generate Summary"):

            with st.spinner("Generating Summary..."):

                summary = generate_summary(
                    st.session_state.rag_chain
                )

            st.write(summary)

    # ---------------- SKILLS ---------------- #

    with skills_tab:

        st.subheader("Technical Skills")

        if st.button("Extract Skills"):

            with st.spinner("Extracting Skills..."):

                skills = extract_skills(
                    st.session_state.rag_chain
                )

            st.write(skills)

    # ---------------- INTERVIEW ---------------- #

    with interview_tab:

        st.subheader("Interview Questions")

        if st.button("Generate Questions"):

            with st.spinner("Generating Questions..."):

                questions = interview_questions(
                    st.session_state.rag_chain
                )

            st.write(questions)

    # ---------------- SUGGESTIONS ---------------- #

    with suggestion_tab:

        st.subheader("Resume Improvement Suggestions")

        if st.button("Generate Suggestions"):

            with st.spinner("Analyzing Resume..."):

                suggestions = improvement_suggestions(
                    st.session_state.rag_chain
                )

            st.write(suggestions)