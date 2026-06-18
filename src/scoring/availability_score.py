from datetime import datetime

def calculate_availability_score(features):

    score = 0

    # Open to work
    if features["open_to_work"]:
        score += 40

    # Notice period
    notice = features["notice_period"]

    if notice <= 30:
        score += 30

    elif notice <= 60:
        score += 20

    else:
        score += 10

    # Last active date

    try:

        last_active = datetime.strptime(
            features["last_active"],
            "%Y-%m-%d"
        )

        days = (
            datetime.now() -
            last_active
        ).days

        if days <= 7:
            score += 30

        elif days <= 30:
            score += 20

        elif days <= 90:
            score += 10

    except:
        pass

    return round(score, 2)