'''
from google import genai

from config import GOOGLE_API_KEY, MODEL_NAME
from src.prompts import RAG_PROMPT

client = genai.Client(api_key=GOOGLE_API_KEY)


def generate_answer(question, docs):

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
'''
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from langchain_google_genai import ChatGoogleGenerativeAI

from config import (
    GOOGLE_API_KEY,
    MODEL_NAME,
)

from src.prompts import RAG_PROMPT


def create_rag_chain(retriever):
    """
    Create a Retrieval-Augmented Generation (RAG) chain.
    """

    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3,
    )

    document_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=RAG_PROMPT,
    )

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain,
    )

    return retrieval_chain