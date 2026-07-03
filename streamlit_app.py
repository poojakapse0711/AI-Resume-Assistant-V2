import os
import streamlit as st

from src.backend import initialize_rag

st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Assistant")

st.markdown("---")

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    os.makedirs("data", exist_ok=True)

    pdf_path = os.path.join(
        "data",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Resume uploaded successfully!")

    with st.spinner("Creating AI Knowledge Base..."):

        rag_chain = initialize_rag(pdf_path)

    st.success("🤖 AI Assistant Ready!")

    question = st.text_input(
        "Ask a question about your resume"
    )

    if st.button("Ask AI"):

        if question.strip() != "":

            with st.spinner("Thinking..."):

                response = rag_chain.invoke(
                    {
                        "input": question
                    }
                )

            st.markdown("## 🤖 Answer")

            st.write(response["answer"])