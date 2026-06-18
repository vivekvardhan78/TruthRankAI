import json

from feature_extractor import extract_candidate_features

with open(
    "data/sample_candidates.json",
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

candidate = candidates[0]

features = extract_candidate_features(candidate)

print("\nFEATURES\n")

for key, value in features.items():
    print(f"{key}: {value}")