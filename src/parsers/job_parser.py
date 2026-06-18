from docx import Document

def extract_text(docx_path):
    doc = Document(docx_path)

    text = []

    for p in doc.paragraphs:
        if p.text.strip():
            text.append(p.text)

    return "\n".join(text)

if __name__ == "__main__":

    content = extract_text(
        "data/job_description.docx"
    )

    print(content)