import json
import faiss
import numpy as np

from app.services.embedding import get_embedding
from app.services.llm import generate_response

# Load data
with open("app/data/data.json", "r") as f:
    data = json.load(f)

texts = [item["content"] for item in data]

embeddings = np.array([get_embedding(text) for text in texts]).astype("float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


def retrieve(query, k=5):
    query_embedding = np.array([get_embedding(query)]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []
    for i, idx in enumerate(indices[0]):
        score = distances[0][i]

        if score < 1.5:
            results.append(data[idx])

    return results


# 🔥 NEW: build conversational context
def build_history_context(history):
    recent = history[-4:]  # last 4 messages only

    context = ""
    for msg in recent:
        role = msg["role"]
        content = msg["content"]
        context += f"{role.upper()}: {content}\n"

    return context


def rag_answer(query, history):
    results = retrieve(query)
    results = results[:3]

    print("\n[RAG] Retrieved Chunks:")
    for r in results:
        print(" -", r["content"])

    context = "\n".join([r["content"] for r in results])

    history_context = build_history_context(history)

    prompt = f"""
You are an educational assistant.

Use both:
1. Context (facts)
2. Conversation history

Be helpful and consistent.

Context:
{context}

Conversation:
{history_context}

User: {query}

Answer:
"""

    return generate_response(prompt)