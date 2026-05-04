from app.services.llm import generate_response

VALID_INTENTS = ["lead_interest", "query"]


def rule_based_intent(message: str):
    msg = message.lower()

    if "interested" in msg or "join" in msg or "enroll" in msg:
        return "lead_interest"

    return None


def llm_intent(message: str):
    prompt = f"""
Classify the user intent into one of these categories:

- lead_interest (user wants to join / shows interest)
- query (user is asking about courses)

Message: "{message}"

Only return one label: lead_interest or query
"""

    response = generate_response(prompt).strip().lower()

    # clean output
    if "lead_interest" in response:
        return "lead_interest"
    elif "query" in response:
        return "query"

    return "query"  # fallback


def detect_intent(message: str):
    # Step 1: Try rule-based
    intent = rule_based_intent(message)

    if intent:
        return intent

    # Step 2: fallback to LLM
    return llm_intent(message)