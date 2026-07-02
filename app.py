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