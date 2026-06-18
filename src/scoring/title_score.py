TARGET_TITLES = [
    "ai engineer",
    "ml engineer",
    "machine learning engineer",
    "recommendation",
    "ranking",
    "search",
    "retrieval",
    "nlp",
    "data scientist"
]

def calculate_title_score(features):

    title = features["current_title"].lower()

    for keyword in TARGET_TITLES:
        if keyword in title:
            return 100

    return 0