import heapq

from src.loaders.large_dataset_loader import (
    load_candidates_stream
)

from src.scoring.feature_extractor import (
    extract_candidate_features
)

from src.filters.fast_prefilter import (
    passes_fast_filter
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

from src.submission.generate_submission import (
    generate_submission
)

TOP_K = 100

top_candidates = []

processed = 0
filtered = 0

for candidate in load_candidates_stream(
    "data/candidates.jsonl"
):

    processed += 1

    try:

        features = extract_candidate_features(
            candidate
        )

        if not passes_fast_filter(
            features
        ):
            continue

        filtered += 1

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

        row = {
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
                product_score
        }

        if len(top_candidates) < TOP_K:

            top_candidates.append(
                row
            )

        else:

            min_score = min(
                top_candidates,
                key=lambda x: x["score"]
            )["score"]

            if final_score > min_score:

                top_candidates.sort(
                    key=lambda x: x["score"]
                )

                top_candidates.pop(0)

                top_candidates.append(
                    row
                )

    except Exception:
        continue

    if filtered % 100 == 0 and filtered > 0:

        print(
            f"Filtered Candidates Processed: {filtered}"
        )

top_candidates = sorted(
    top_candidates,
    key=lambda x: x["score"],
    reverse=True
)

print("\nTOP 20 CANDIDATES\n")

for rank, item in enumerate(
    top_candidates[:20],
    start=1
):

    print(
        f"{rank}. "
        f"{item['candidate_id']} | "
        f"{item['title']} | "
        f"Final={round(item['score'],2)} | "
        f"Semantic={round(item['semantic'],2)} | "
        f"CareerFit={item['career_fit']}"
    )

print("\nTOTAL:", processed)
print("FILTERED:", filtered)

generate_submission(
    top_candidates
)

print(
    "\nTop 100 submission file generated successfully."
)