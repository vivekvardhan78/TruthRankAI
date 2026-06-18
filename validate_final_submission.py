import pandas as pd

df = pd.read_csv(
    "outputs/final_submission.csv"
)

print("\nVALIDATION REPORT\n")

# 1. Exactly 100 rows

if len(df) == 100:
    print("PASS: Exactly 100 rows")
else:
    print(
        f"FAIL: Found {len(df)} rows"
    )

# 2. Rank starts at 1

if df["rank"].min() == 1:
    print("PASS: Rank starts at 1")
else:
    print("FAIL: Rank does not start at 1")

# 3. Rank ends at 100

if df["rank"].max() == 100:
    print("PASS: Rank ends at 100")
else:
    print("FAIL: Rank does not end at 100")

# 4. Duplicate IDs

duplicates = df[
    "candidate_id"
].duplicated().sum()

if duplicates == 0:
    print("PASS: No duplicate candidate_ids")
else:
    print(
        f"FAIL: {duplicates} duplicate IDs"
    )

# 5. Score monotonic

scores = df["score"].tolist()

valid = True

for i in range(
    len(scores) - 1
):

    if scores[i] < scores[i + 1]:
        valid = False
        break

if valid:
    print(
        "PASS: Scores decrease with rank"
    )
else:
    print(
        "FAIL: Score ordering incorrect"
    )

# 6. Not all same score

if len(
    df["score"].unique()
) > 1:

    print(
        "PASS: Scores differentiated"
    )

else:

    print(
        "FAIL: All scores identical"
    )

print("\nValidation Complete")