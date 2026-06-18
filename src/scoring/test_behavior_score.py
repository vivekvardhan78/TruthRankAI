import json

from feature_extractor import extract_candidate_features
from behavior_score import calculate_behavior_score

with open(
    "data/sample_candidates.json",
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

features = extract_candidate_features(
    candidates[0]
)

score = calculate_behavior_score(
    features
)

print()
print("BEHAVIOR SCORE")
print(score)