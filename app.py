'''from src.loader import load_documents


def main():

    docs = load_documents()

    print(f"Total Pages : {len(docs)}")

    print("=" * 60)

    print(docs[0].page_content)


if __name__ == "__main__":

    main()
 '''   
'''    
from src.loader import load_documents
from src.splitter import split_documents


def main():

    documents = load_documents()

    chunks = split_documents(documents)

    print(f"Pages Loaded : {len(documents)}")
    print(f"Chunks Created : {len(chunks)}")

    print("=" * 60)

    print(chunks[0].page_content)

    print("=" * 60)

    print(chunks[0].metadata)


if __name__ == "__main__":
    main()
    
'''
'''
from src.loader import load_documents
from src.splitter import split_documents
from src.vector_store import create_vector_store


def main():

    print("=" * 60)
    print("AI Resume Assistant")
    print("=" * 60)

    print("\nLoading PDF...")
    documents = load_documents()

    print("Splitting Documents...")
    chunks = split_documents(documents)

    print(f"Total Chunks : {len(chunks)}")

    print("\nCreating Vector Store...")

    create_vector_store(chunks)

    print("\n✅ Vector Database Created Successfully!")

    print("\nSaved in:")
    print("faiss_index/")


if __name__ == "__main__":
    main()
    
'''
'''
from src.loader import load_documents
from src.splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import load_retriever


def main():

    print("=" * 60)
    print("📄 AI Resume Assistant")
    print("=" * 60)

    # Build Vector DB
    documents = load_documents()

    chunks = split_documents(documents)

    create_vector_store(chunks)

    print("\n✅ Vector Store Ready!")

    retriever = load_retriever()

    print("\n🤖 Ask questions about your resume.")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye 👋")
            break

        docs = retriever.invoke(question)

        print("\n📌 Retrieved Chunks:\n")

        for i, doc in enumerate(docs, start=1):
            print("=" * 60)
            print(f"Chunk {i}")
            print("=" * 60)
            print(doc.page_content)
            print()


if __name__ == "__main__":
    main()
    
'''

from src.loader import load_documents
from src.splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import load_retriever
from src.rag_chain import generate_answer


def main():

    print("=" * 60)
    print("📄 AI Resume Assistant")
    print("=" * 60)

    # Step 1: Load Resume
    print("\n📖 Loading Resume...")
    documents = load_documents()

    # Step 2: Split Resume
    print("✂️ Splitting Resume...")
    chunks = split_documents(documents)

    print(f"✅ Total Chunks Created: {len(chunks)}")

    # Step 3: Create Vector Store
    print("\n🧠 Creating Vector Database...")
    create_vector_store(chunks)

    print("✅ Vector Database Ready!")

    # Step 4: Load Retriever
    retriever = load_retriever()

    print("\n🤖 AI Resume Assistant is Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ").strip()

        if question.lower() == "exit":
            print("\n👋 Thank you for using AI Resume Assistant!")
            break

        if question == "":
            print("⚠️ Please enter a question.\n")
            continue

        # Retrieve relevant resume chunks
        docs = retriever.invoke(question)

        # Generate answer using Gemini
        answer = generate_answer(question, docs)

        print("\n" + "=" * 60)
        print("🤖 AI Resume Assistant")
        print("=" * 60)
        print(answer)
        print("=" * 60)


if __name__ == "__main__":
    main()
    


