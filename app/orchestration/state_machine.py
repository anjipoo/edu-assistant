from app.services.lead import save_lead

def handle_state(session, message):
    state = session.get("state", "idle")

    if state == "collecting_name":
        session["lead_data"]["name"] = message
        session["state"] = "collecting_course"
        return "Which course are you interested in?"

    elif state == "collecting_course":
        session["lead_data"]["course"] = message
        session["state"] = "collecting_contact"
        return "Please share your contact number."

    elif state == "collecting_contact":
        session["lead_data"]["contact"] = message

        save_lead(session["lead_data"])

        session["state"] = "idle"
        return "Thank you! Our team will contact you soon."

    return None