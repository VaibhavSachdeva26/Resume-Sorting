from PyPDF2 import PdfReader
import docx


def extract_text(file):
    if file.type == "application/pdf":
        return extract_pdf_text(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_docx_text(file)


def extract_pdf_text(file):
    print("inside extract pdf text method..")

    reader = PdfReader(file)
    pdf_text = ""

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        pdf_text += page.extract_text() + "\n"

        return pdf_text


def extract_docx_text(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])
