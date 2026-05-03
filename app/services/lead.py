leads = []

def calculate_score(lead_data, interaction_flags):
    score = 0

    if interaction_flags.get("asked_fees"):
        score += 2

    if interaction_flags.get("asked_details"):
        score += 2

    if interaction_flags.get("showed_interest"):
        score += 3

    if lead_data.get("contact"):
        score += 5

    return score


def classify_lead(score):
    if score >= 8:
        return "HOT 🔥"
    elif score >= 4:
        return "WARM"
    else:
        return "COLD"


def save_lead(lead_data, interaction_flags):
    score = calculate_score(lead_data, interaction_flags)
    category = classify_lead(score)

    lead_data["score"] = score
    lead_data["category"] = category

    leads.append(lead_data)

    print("\n[LEAD SAVED]")
    print(lead_data)