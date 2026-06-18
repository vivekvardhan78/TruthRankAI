import json

from src.scoring.feature_extractor import (
    extract_candidate_features
)

from src.scoring.role_match_score import (
    calculate_role_match
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

with open(
    "data/sample_candidates.json",
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

candidate = candidates[0]

features = extract_candidate_features(candidate)

role_score, _ = calculate_role_match(features)

product_score, _ = calculate_product_experience(features)

behavior_score = calculate_behavior_score(features)

availability_score = calculate_availability_score(features)

final_score = calculate_final_score(
    role_score,
    product_score,
    behavior_score,
    availability_score
)

print("\nROLE:", role_score)
print("PRODUCT:", product_score)
print("BEHAVIOR:", behavior_score)
print("AVAILABILITY:", availability_score)

print("\nFINAL SCORE:", final_score)