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