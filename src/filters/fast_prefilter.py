import re

AI_KEYWORDS = [

    "machine learning",
    "ml engineer",
    "ai engineer",

    "retrieval",
    "ranking",
    "recommendation",

    "search engineer",

    "nlp",

    "llm",

    "data scientist",

    "applied ml",

    "embeddings",

    "faiss",
    "pinecone",
    "qdrant",
    "milvus",

    "sentence transformers",

    "information retrieval"
]


def passes_fast_filter(features):

    text = " ".join([

        features["current_title"],

        features["headline"],

        features["summary"],

        features["career_text"]

    ]).lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    matches = 0

    for keyword in AI_KEYWORDS:

        if keyword.lower() in text:
            matches += 1

    return matches >= 2