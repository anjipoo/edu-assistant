import json
import faiss
import numpy as np

from app.services.embedding import get_embedding
from app.services.llm import generate_response

# Load dataset
with open("app/data/data.json", "r") as f:
    data = json.load(f)

texts = [item["content"] for item in data]

# Create embeddings
embeddings = np.array([get_embedding(text) for text in texts]).astype("float32")

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


def retrieve(query, k=5):
    query_embedding = np.array([get_embedding(query)]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []
    for i, idx in enumerate(indices[0]):
        score = distances[0][i]

        # filter weak matches
        if score < 1.5:
            results.append(data[idx])

    return results


def rag_answer(query):
    results = retrieve(query)

    # limit context
    results = results[:3]

    print("\n[RAG] Retrieved Chunks:")
    for r in results:
        print(" -", r["content"])

    context = "\n".join([r["content"] for r in results])

    prompt = f"""
You are an educational assistant.

Answer ONLY using the context below.
Be clear, concise, and helpful.

Context:
{context}

User: {query}

Answer:
"""

    return generate_response(prompt)