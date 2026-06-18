def calculate_final_score(
    semantic_score,
    product_score,
    behavior_score,
    availability_score,
    career_fit_score
):

    score = (

        semantic_score * 0.35 +

        career_fit_score * 0.35 +

        product_score * 0.15 +

        behavior_score * 0.10 +

        availability_score * 0.05

    )

    return round(score, 2)