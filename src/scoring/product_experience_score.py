PRODUCT_KEYWORDS = [

    "retrieval",
    "search",
    "ranking",
    "recommendation",

    "candidate matching",

    "embeddings",

    "vector database",

    "faiss",
    "pinecone",
    "qdrant",
    "milvus",

    "ndcg",
    "mrr",
    "map",

    "ab testing",

    "re-ranking"
]


def calculate_product_experience(features):

    text = (
        features["career_text"] +
        " " +
        features["summary"]
    ).lower()

    score = 0

    matches = []

    for keyword in PRODUCT_KEYWORDS:

        if keyword in text:

            score += 1
            matches.append(keyword)

    final_score = min(
        100,
        score * 10
    )

    return final_score, matches