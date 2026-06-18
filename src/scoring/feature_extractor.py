def extract_candidate_features(candidate):

    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    skills = [
        skill["name"]
        for skill in candidate["skills"]
    ]

    career_text = " ".join([
        job["description"]
        for job in candidate["career_history"]
    ])

    return {

        "candidate_id": candidate["candidate_id"],

        "headline": profile["headline"],
        "summary": profile["summary"],

        "current_title": profile["current_title"],
        "current_company": profile["current_company"],

        "years_experience": profile["years_of_experience"],

        "skills": skills,

        "career_text": career_text,

        "open_to_work": signals["open_to_work_flag"],

        "response_rate": signals["recruiter_response_rate"],

        "github_score": signals["github_activity_score"],

        "interview_completion":
            signals["interview_completion_rate"],

        "profile_completeness":
            signals["profile_completeness_score"],

        "notice_period":
            signals["notice_period_days"],

        "last_active":
            signals["last_active_date"]
    }