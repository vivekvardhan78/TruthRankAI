import json

from feature_extractor import (
    extract_candidate_features
)

from product_experience_score import (
    calculate_product_experience
)

with open(
    "data/sample_candidates.json",
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

features = extract_candidate_features(
    candidates[0]
)

score, matches = (
    calculate_product_experience(
        features
    )
)

print()

print("PRODUCT EXPERIENCE SCORE")
print(score)

print()

print("MATCHES")

for m in matches:
    print("-", m)