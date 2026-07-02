from src.loader import load_documents


def main():

    docs = load_documents()

    print(f"Total Pages : {len(docs)}")

    print("=" * 60)

    print(docs[0].page_content)


if __name__ == "__main__":

    main()