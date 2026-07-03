'''
from langchain_community.document_loaders import PyPDFLoader

from config import PDF_PATH


def load_documents():

    loader = PyPDFLoader(PDF_PATH)

    documents = loader.load()

    return documents
'''

from langchain_community.document_loaders import PyPDFLoader


def load_documents(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents