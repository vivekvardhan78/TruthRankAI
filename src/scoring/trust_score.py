def calculate_trust_score(candidate):

    trust = 100

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    if not signals.get(
        "verified_email",
        False
    ):
        trust -= 20

    if not signals.get(
        "verified_phone",
        False
    ):
        trust -= 20

    profile_score = signals.get(
        "profile_completeness_score",
        0
    )

    if profile_score < 50:
        trust -= 15

    response_rate = signals.get(
        "recruiter_response_rate",
        0
    )

    if response_rate < 0.10:
        trust -= 15

    interview_rate = signals.get(
        "interview_completion_rate",
        0
    )

    if interview_rate < 0.20:
        trust -= 10

    return max(
        0,
        trust
    )