from app.services.llm import generate_response

def generate_followup(lead_data):
    name = lead_data.get("name", "there")
    course = lead_data.get("course", "the course")

    prompt = f"""
You are an educational assistant.

Write a short, friendly follow-up message for a user who showed interest in {course}.

Personalize it using the name: {name}

Keep it:
- professional
- engaging
- concise (2-3 lines)

Message:
"""

    return generate_response(prompt)