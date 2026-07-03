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

# ---------- Session State ----------

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Upload Resume ----------

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

    st.success("✅ Resume Uploaded!")

    with st.spinner("Creating AI Knowledge Base..."):

        st.session_state.rag_chain = initialize_rag(pdf_path)

    st.success("🤖 AI Assistant Ready!")

# ---------- Display Chat History ----------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------- Chat ----------

if st.session_state.rag_chain is not None:

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