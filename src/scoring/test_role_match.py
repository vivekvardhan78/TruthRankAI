import json

from feature_extractor import (
    extract_candidate_features
)

from role_match_score import (
    calculate_role_match
)

with open(
    "data/sample_candidates.json",
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

candidate = candidates[0]

features = extract_candidate_features(
    candidate
)

score, matched = calculate_role_match(
    features
)

print()

print("ROLE MATCH SCORE")
print(score)

print()

print("MATCHED KEYWORDS")

for item in matched:
    print("-", item)