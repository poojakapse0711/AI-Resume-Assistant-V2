from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from config import (
    GOOGLE_API_KEY,
    EMBEDDING_MODEL,
    VECTOR_DB_PATH,
)


def create_vector_store(chunks):
    """
    Create a FAISS vector store and save it locally.
    """

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY,
    )

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings,
    )

    vector_store.save_local(VECTOR_DB_PATH)

    return vector_store