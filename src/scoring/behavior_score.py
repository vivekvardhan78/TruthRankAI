def calculate_behavior_score(features):

    score = 0

    score += features["response_rate"] * 30

    score += features["interview_completion"] * 25

    score += (features["profile_completeness"] / 100) * 25

    score += (features["github_score"] / 10) * 20

    return round(score, 2)