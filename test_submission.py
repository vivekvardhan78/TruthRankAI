from src.submission.generate_submission import (
    generate_submission
)

sample = [

    {
        "candidate_id": "CAND_001",
        "title": "AI Engineer",
        "score": 90.5
    },

    {
        "candidate_id": "CAND_002",
        "title": "ML Engineer",
        "score": 88.3
    }

]

generate_submission(sample)