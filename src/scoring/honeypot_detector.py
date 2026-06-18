BAD_TITLES = [

    "marketing manager",

    "sales manager",

    "graphic designer",

    "accountant",

    "civil engineer",

    "mechanical engineer"

]


def honeypot_penalty(
    title,
    semantic_score
):

    title = title.lower()

    if (
        title in BAD_TITLES
        and semantic_score > 75
    ):
        return 30

    return 0