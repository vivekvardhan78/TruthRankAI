import pandas as pd


def generate_submission(rows):

    submission_rows = []

    for rank, row in enumerate(
        rows,
        start=1
    ):

        submission_rows.append({

            "candidate_id":
                row["candidate_id"],

            "rank":
                rank,

            "score":
                round(
                    row["score"],
                    6
                ),

            "reasoning":
                row["reasoning"]

        })

    df = pd.DataFrame(

        submission_rows,

        columns=[
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]

    )

    df.to_csv(
        "outputs/final_submission.csv",
        index=False
    )

    print(
        "\nSubmission generated successfully!"
    )