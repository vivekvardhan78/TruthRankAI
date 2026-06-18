import pandas as pd

from src.explainability.explanation_generator import (
    generate_explanation
)

submission = pd.read_csv(
    "outputs/final_submission.csv"
)

rows = []

for _, row in submission.iterrows():

    explanation = generate_explanation(

        semantic_score=85,

        career_fit_score=80,

        product_score=30

    )

    rows.append({

        "candidate_id":
            row["candidate_id"],

        "title":
            row["title"],

        "score":
            row["score"],

        "explanation":
            explanation

    })

df = pd.DataFrame(rows)

df.to_csv(

    "outputs/candidate_explanations.csv",

    index=False

)

print(
    "candidate_explanations.csv generated"
)