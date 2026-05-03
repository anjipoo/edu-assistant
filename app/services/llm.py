import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def generate_response(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]