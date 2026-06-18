from src.loaders.large_dataset_loader import (
    load_candidates_stream
)

from src.scoring.feature_extractor import (
    extract_candidate_features
)

from src.filters.fast_prefilter import (
    passes_fast_filter
)

count_all = 0
count_filtered = 0

for candidate in load_candidates_stream(
    "data/candidates.jsonl"
):

    count_all += 1

    features = extract_candidate_features(
        candidate
    )

    if passes_fast_filter(features):
        count_filtered += 1

print()

print("TOTAL:", count_all)

print("FILTERED:", count_filtered)