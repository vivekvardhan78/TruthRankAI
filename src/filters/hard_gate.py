def passes_hard_gate(
    semantic_score,
    career_fit_score
):

    if semantic_score < 65:
        return False

    if career_fit_score < 20:
        return False

    return True