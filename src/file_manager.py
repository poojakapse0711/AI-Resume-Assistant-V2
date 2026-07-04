import os


def save_uploaded_pdf(uploaded_file):
    """
    Save the uploaded PDF to the data folder
    and return its file path.
    """

    os.makedirs("data", exist_ok=True)

    pdf_path = os.path.join(
        "data",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    return pdf_path