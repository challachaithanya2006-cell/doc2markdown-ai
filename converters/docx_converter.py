from docx import Document


def convert_docx(file_path):

    doc = Document(file_path)

    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)