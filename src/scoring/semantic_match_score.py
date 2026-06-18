from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from docx import Document


# Load model only once
model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def load_job_description():

    doc = Document(
        "data/job_description.docx"
    )

    text = []

    for paragraph in doc.paragraphs:

        if paragraph.text.strip():

            text.append(
                paragraph.text.strip()
            )

    return "\n".join(text)


# Load JD once during startup
JD_TEXT = load_job_description()


def calculate_semantic_score(features):

    candidate_text = " ".join([

        features["headline"],

        features["summary"],

        features["career_text"],

        " ".join(features["skills"])

    ])

    jd_embedding = model.encode(
        JD_TEXT,
        normalize_embeddings=True
    )

    candidate_embedding = model.encode(
        candidate_text,
        normalize_embeddings=True
    )

    similarity = cosine_similarity(
        [jd_embedding],
        [candidate_embedding]
    )[0][0]

    return round(
        similarity * 100,
        2
    )