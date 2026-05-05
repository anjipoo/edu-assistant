from app.services.lead import save_lead
from app.services.followup import generate_followup

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

        # Save lead
        save_lead(
            session["lead_data"],
            session["interaction_flags"]
        )

        # 🔥 Generate follow-up
        followup_msg = generate_followup(session["lead_data"])

        session["state"] = "idle"
        session["interaction_flags"] = {
            "asked_fees": False,
            "asked_details": False,
            "showed_interest": False
        }

        return f"Thank you! Our team will contact you soon.\n\n{followup_msg}"

    return None