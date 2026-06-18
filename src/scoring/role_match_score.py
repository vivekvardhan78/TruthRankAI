import re

TARGET_KEYWORDS = [

    "retrieval",
    "ranking",
    "recommendation",

    "embeddings",
    "vector",

    "faiss",
    "pinecone",
    "qdrant",
    "milvus",

    "llm",
    "fine-tuning",

    "search",

    "ndcg",
    "mrr",
    "map"
]


def calculate_role_match(features):

    text = " ".join([

        features["headline"],
        features["summary"],
        features["career_text"],
        " ".join(features["skills"])

    ]).lower()

    score = 0

    matched = []

    for keyword in TARGET_KEYWORDS:

        if re.search(keyword, text):

            score += 1
            matched.append(keyword)

    score = min(
        100,
        (score / len(TARGET_KEYWORDS)) * 100
    )

    return round(score, 2), matched