import heapq

from src.loaders.large_dataset_loader import (
    load_candidates_stream
)

from src.scoring.feature_extractor import (
    extract_candidate_features
)

from src.scoring.semantic_match_score import (
    calculate_semantic_score
)

from src.scoring.career_fit_score import (
    calculate_career_fit
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

from src.ranking.hybrid_ranker import (
    calculate_final_score
)

TOP_K = 100

top_candidates = []

count = 0

for candidate in load_candidates_stream(
    "data/candidates.jsonl"
):

    count += 1

    try:

        features = extract_candidate_features(
            candidate
        )

        semantic_score = (
            calculate_semantic_score(
                features
            )
        )

        career_fit_score = (
            calculate_career_fit(
                features
            )
        )

        product_score, _ = (
            calculate_product_experience(
                features
            )
        )

        behavior_score = (
            calculate_behavior_score(
                features
            )
        )

        availability_score = (
            calculate_availability_score(
                features
            )
        )

        final_score = (
            calculate_final_score(
                semantic_score,
                career_fit_score,
                product_score,
                behavior_score,
                availability_score
            )
        )

        row = (
            final_score,
            candidate["candidate_id"],
            features["current_title"]
        )

        if len(top_candidates) < TOP_K:

            heapq.heappush(
                top_candidates,
                row
            )

        else:

            heapq.heappushpop(
                top_candidates,
                row
            )

    except Exception:
        continue

    if count % 5000 == 0:

        print(
            f"Processed {count} candidates..."
        )

top_candidates.sort(
    reverse=True
)

print("\nTOP 20\n")

for rank, item in enumerate(
    top_candidates[:20],
    start=1
):

    print(
        rank,
        item[1],
        item[2],
        item[0]
    )