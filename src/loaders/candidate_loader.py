import json
from pprint import pprint

with open(
    "data/sample_candidates.json",
    "r",
    encoding="utf-8"
) as f:

    candidates = json.load(f)

candidate = candidates[0]

print("\n===== PROFILE =====")
pprint(candidate["profile"])

print("\n===== CAREER HISTORY =====")
pprint(candidate["career_history"][0])

print("\n===== SKILLS =====")
pprint(candidate["skills"][:5])

print("\n===== REDROB SIGNALS =====")
pprint(candidate["redrob_signals"])