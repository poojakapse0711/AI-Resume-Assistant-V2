'''from src.loader import load_documents


def main():

    docs = load_documents()

    print(f"Total Pages : {len(docs)}")

    print("=" * 60)

    print(docs[0].page_content)


if __name__ == "__main__":

    main()
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