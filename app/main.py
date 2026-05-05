from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.admin import router as admin_router

app = FastAPI()

app.include_router(chat_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {"message": "AI Assistant"}