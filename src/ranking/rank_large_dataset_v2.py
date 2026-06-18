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

from src.scoring.trust_score import (
    calculate_trust_score
)

from src.scoring.honeypot_detector import (
    honeypot_penalty
)

from src.ranking.hybrid_ranker import (
    calculate_final_score
)

from src.submission.generate_submission import (
    generate_submission
)

from src.explainability.explanation_generator import (
    generate_explanation
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

        trust_score = (
            calculate_trust_score(
                candidate
            )
        )

        penalty = (
            honeypot_penalty(
                features["current_title"],
                semantic_score
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

        # Trust Bonus
        final_score += (
            trust_score * 0.05
        )

        # Honeypot Penalty
        final_score -= penalty

        # Clamp score
        final_score = max(
            0,
            min(
                100,
                final_score
            )
        )

        row = (

            final_score,

            candidate["candidate_id"],

            features["current_title"],

            semantic_score,

            career_fit_score,

            product_score,

            trust_score

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

    if filtered % 100 == 0 and filtered > 0:

        print(
            f"Filtered Candidates Processed: {filtered}"
        )

top_candidates.sort(
    reverse=True
)

print("\nTOP 20 CANDIDATES\n")

for rank, item in enumerate(
    top_candidates[:20],
    start=1
):

    print(
        f"{rank}. "
        f"{item[1]} | "
        f"{item[2]} | "
        f"Final={round(item[0],2)} | "
        f"Semantic={round(item[3],2)} | "
        f"CareerFit={item[4]} | "
        f"Trust={item[6]}"
    )

print("\nTOTAL:", processed)
print("FILTERED:", filtered)

# Build Submission

submission_rows = []

for item in top_candidates:

    reasoning = generate_explanation(

        title=item[2],

        semantic_score=item[3],

        career_fit_score=item[4],

        product_score=item[5]

    )

    submission_rows.append({

        "candidate_id":
            item[1],

        "score":
            item[0],

        "reasoning":
            reasoning

    })

generate_submission(
    submission_rows
)

print(
    "\nTop 100 submission file generated successfully."
)