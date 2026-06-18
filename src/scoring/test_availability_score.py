import json

from feature_extractor import extract_candidate_features
from availability_score import calculate_availability_score

with open(
    "data/sample_candidates.json",
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

features = extract_candidate_features(
    candidates[0]
)

score = calculate_availability_score(
    features
)

print()
print("AVAILABILITY SCORE")
print(score)