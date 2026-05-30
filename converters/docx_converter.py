from docx import Document

def convert_docx(file_path):
    doc=Document(file_path)
    return "\n".join(p.text for p in doc.paragraphs)
