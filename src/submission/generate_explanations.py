import pandas as pd


def save_explanations(rows):

    df = pd.DataFrame(rows)

    df.to_csv(
        "outputs/candidate_explanations.csv",
        index=False
    )

    print(
        "\nExplanations saved successfully!"
    )

    print(
        "outputs/candidate_explanations.csv"
    )