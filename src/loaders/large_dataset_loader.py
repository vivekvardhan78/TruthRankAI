import json


def load_candidates_stream(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            yield json.loads(line)


if __name__ == "__main__":

    count = 0

    for candidate in load_candidates_stream(
        "data/candidates.jsonl"
    ):

        count += 1

        if count <= 3:

            print(
                candidate["candidate_id"]
            )

    print(
        f"\nTotal Checked: {count}"
    )