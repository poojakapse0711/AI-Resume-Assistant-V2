import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

MODEL_NAME = "gemini-2.5-flash"

EMBEDDING_MODEL = "models/gemini-embedding-001"

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

PDF_PATH = "data/resume.pdf"

VECTOR_DB_PATH = "faiss_index"

TEMPERATURE = 0.3

TOP_K = 3