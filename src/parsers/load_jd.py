from docx import Document

def load_job_description():

    doc = Document(
        "data/job_description.docx"
    )

    text = []

    for p in doc.paragraphs:
        if p.text.strip():
            text.append(p.text)

    return "\n".join(text)