sessions = {}

def get_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = {
            "state": "idle",
            "lead_data": {},
            "interaction_flags": {
                "asked_fees": False,
                "asked_details": False,
                "showed_interest": False
            }
        }

    return sessions[session_id]