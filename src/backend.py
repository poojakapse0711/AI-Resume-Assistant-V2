import os

from src.loader import load_documents
from src.splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import load_retriever
from src.rag_chain import create_rag_chain


def initialize_rag():

    documents = load_documents()

    chunks = split_documents(documents)

    if not os.path.exists("faiss_index"):

        create_vector_store(chunks)

    retriever = load_retriever()

    rag_chain = create_rag_chain(retriever)

    return rag_chain