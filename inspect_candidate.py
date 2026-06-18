import json
from pprint import pprint

with open(
    "data/sample_candidates.json",
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

candidate = candidates[30]   # CAND_0000031

print("\nPROFILE\n")
pprint(candidate["profile"])

print("\nCAREER HISTORY\n")
for item in candidate["career_history"]:
    pprint(item)

print("\nSKILLS\n")
pprint(candidate["skills"])