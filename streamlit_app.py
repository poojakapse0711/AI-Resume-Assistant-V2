'''
import streamlit as st

st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Assistant")

st.write(
    "Welcome to your AI Resume Assistant built using "
    "Gemini + LangChain + FAISS."
)

st.success("Streamlit is working successfully!")
'''
import streamlit as st

from src.backend import initialize_rag

st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 AI Resume Assistant")

st.markdown("---")

st.write(
    "Ask questions about your resume using Gemini + LangChain + FAISS."
)

with st.spinner("Loading AI Resume Assistant..."):

    rag_chain = initialize_rag()

st.success("AI Resume Assistant Ready!")

question = st.text_input(
    "Ask a question"
)

if st.button("Ask AI"):

    if question.strip() != "":

        with st.spinner("Thinking..."):

            response = rag_chain.invoke(
                {
                    "input": question
                }
            )

        st.markdown("### 🤖 Answer")

        st.write(response["answer"])