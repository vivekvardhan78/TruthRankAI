GOOD_TITLES = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "recommendation",
    "search engineer",
    "retrieval",
    "nlp engineer",
    "applied ml engineer",
    "data scientist"
]

def calculate_title_relevance(features):

    title = features["current_title"].lower()

    for keyword in GOOD_TITLES:

        if keyword in title:
            return 100

    return 0