from fastapi import APIRouter
from pydantic import BaseModel

from app.services.rag import rag_answer
from app.services.intent import detect_intent
from app.orchestration.session import get_session
from app.orchestration.state_machine import handle_state
from app.core.logger import log_step

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    message: str


@router.post("/chat")
def chat(req: ChatRequest):
    session = get_session(req.session_id)

    log_step("USER", req.message)

    # 🔥 Save message to history
    session["history"].append({"role": "user", "content": req.message})

    # Update interaction flags
    msg = req.message.lower()

    if "fee" in msg or "cost" in msg:
        session["interaction_flags"]["asked_fees"] = True

    if "course" in msg or "details" in msg:
        session["interaction_flags"]["asked_details"] = True

    # Handle lead flow
    state_response = handle_state(session, req.message)
    if state_response:
        session["history"].append({"role": "assistant", "content": state_response})

        log_step("STATE", session["state"])
        log_step("RESPONSE", state_response)

        return {
            "state": session["state"],
            "response": state_response
        }

    # Intent detection
    intent = detect_intent(req.message)
    log_step("INTENT", intent)

    if intent == "lead_interest":
        session["state"] = "collecting_name"
        session["interaction_flags"]["showed_interest"] = True

        response = "Great! Can I have your name?"

        session["history"].append({"role": "assistant", "content": response})

        log_step("STATE", session["state"])
        log_step("RESPONSE", response)

        return {
            "state": session["state"],
            "response": response
        }

    # 🔥 RAG WITH CONTEXT
    response = rag_answer(req.message, session["history"])

    session["history"].append({"role": "assistant", "content": response})

    log_step("STATE", session["state"])
    log_step("RESPONSE", response)

    return {
        "intent": intent,
        "state": session["state"],
        "response": response
    }