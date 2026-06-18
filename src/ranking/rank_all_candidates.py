import json

from src.scoring.feature_extractor import (
    extract_candidate_features
)

from src.scoring.semantic_match_score import (
    calculate_semantic_score
)

from src.scoring.product_experience_score import (
    calculate_product_experience
)

from src.scoring.behavior_score import (
    calculate_behavior_score
)

from src.scoring.availability_score import (
    calculate_availability_score
)

from src.scoring.career_fit_score import (
    calculate_career_fit
)

from src.ranking.hybrid_ranker import (
    calculate_final_score
)


BAD_TITLES = [
    "accountant",
    "graphic designer",
    "civil engineer",
    "hr manager",
    "marketing manager",
    "operations manager"
]


with open(
    "data/sample_candidates.json",
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

results = []

for candidate in candidates:

    features = extract_candidate_features(candidate)

    title = features["current_title"].lower()

    if title in BAD_TITLES:
        continue

    semantic_score = calculate_semantic_score(
        features
    )

    career_fit_score = calculate_career_fit(
        features
    )

    product_score, _ = calculate_product_experience(
        features
    )

    behavior_score = calculate_behavior_score(
        features
    )

    availability_score = calculate_availability_score(
        features
    )

    final_score = calculate_final_score(
        semantic_score,
        career_fit_score,
        product_score,
        behavior_score,
        availability_score
    )

    results.append({

        "candidate_id":
            candidate["candidate_id"],

        "title":
            features["current_title"],

        "score":
            final_score,

        "semantic":
            semantic_score,

        "career_fit":
            career_fit_score,

        "product":
            product_score,

        "behavior":
            behavior_score,

        "availability":
            availability_score

    })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTOP 10 CANDIDATES\n")

for i, row in enumerate(
    results[:10],
    start=1
):

    print(
        f"{i}. "
        f"{row['candidate_id']} | "
        f"{row['title']} | "
        f"Final={row['score']} | "
        f"Semantic={row['semantic']} | "
        f"CareerFit={row['career_fit']} | "
        f"Product={row['product']}"
    )