import json
import pandas as pd

submission = pd.read_csv(
    "outputs/final_submission.csv"
)

valid_ids = set()

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        candidate = json.loads(
            line
        )

        valid_ids.add(
            candidate["candidate_id"]
        )

missing = []

for cid in submission[
    "candidate_id"
]:

    if cid not in valid_ids:

        missing.append(
            cid
        )

print()

if len(missing) == 0:

    print(
        "PASS: All candidate_ids exist in dataset"
    )

else:

    print(
        "FAIL:"
    )

    for item in missing:

        print(item)