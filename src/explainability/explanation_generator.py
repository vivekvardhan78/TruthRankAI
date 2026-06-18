def generate_explanation(
    title,
    semantic_score,
    career_fit_score,
    product_score
):

    reasons = []

    if semantic_score >= 80:

        reasons.append(
            f"{title} shows strong semantic alignment with the role"
        )

    if career_fit_score >= 70:

        reasons.append(
            "Direct experience in retrieval, ranking, search or AI systems"
        )

    if product_score >= 20:

        reasons.append(
            "Demonstrated production-scale ML experience"
        )

    if len(reasons) == 0:

        reasons.append(
            "Overall profile relevance"
        )

    return ". ".join(reasons)