import json

from src.scoring.feature_extractor import (
    extract_candidate_features
)

from src.scoring.semantic_match_score import (
    calculate_semantic_score
)

with open(
    "data/sample_candidates.json",
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

features = extract_candidate_features(
    candidates[30]
)

score = calculate_semantic_score(
    features
)

print()
print("SEMANTIC SCORE")
print(score)