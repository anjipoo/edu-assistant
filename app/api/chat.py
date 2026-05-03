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

    # Step 1: Handle ongoing state (lead flow)
    state_response = handle_state(session, req.message)
    if state_response:
        log_step("STATE", session["state"])
        log_step("RESPONSE", state_response)
        return {
            "state": session["state"],
            "response": state_response
        }

    # Step 2: Detect intent
    intent = detect_intent(req.message)
    log_step("INTENT", intent)

    # Step 3: Handle interest
    if intent == "lead_interest":
        session["state"] = "collecting_name"
        response = "Great! Can I have your name?"

        log_step("STATE", session["state"])
        log_step("RESPONSE", response)

        return {
            "state": session["state"],
            "response": response
        }

    # Step 4: RAG response
    response = rag_answer(req.message)

    log_step("STATE", session["state"])
    log_step("RESPONSE", response)

    return {
        "intent": intent,
        "state": session["state"],
        "response": response
    }