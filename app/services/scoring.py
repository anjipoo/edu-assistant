def calculate_score(session):
    score = 0

    # Interest detected
    if session.get("interested"):
        score += 3

    # Asked queries
    score += session.get("query_count", 0) * 2

    # Contact provided
    if "contact" in session.get("lead_data", {}):
        score += 5

    return score


def classify_lead(score):
    if score >= 7:
        return "hot"
    elif score >= 4:
        return "warm"
    else:
        return "cold"