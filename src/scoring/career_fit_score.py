AI_TITLES = [

    "ai engineer",
    "ml engineer",
    "machine learning engineer",

    "recommendation",

    "search engineer",

    "retrieval",

    "nlp engineer",

    "applied ml",

    "data scientist"
]


def calculate_career_fit(features):

    title = features["current_title"].lower()

    score = 0

    for keyword in AI_TITLES:

        if keyword in title:

            score += 50

    career_text = features[
        "career_text"
    ].lower()

    CAREER_KEYWORDS = [

        "retrieval",
        "ranking",
        "recommendation",

        "search",

        "embeddings",

        "faiss",
        "pinecone",
        "qdrant",
        "milvus",

        "ndcg",
        "mrr",
        "map",

        "ab test",

        "learning-to-rank",

        "semantic search"
    ]

    for keyword in CAREER_KEYWORDS:

        if keyword in career_text:

            score += 5

    return min(score, 100)