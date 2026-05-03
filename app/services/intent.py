def detect_intent(message: str):
    msg = message.lower()

    if "interested" in msg or "join" in msg or "enroll" in msg:
        return "lead_interest"

    return "query"