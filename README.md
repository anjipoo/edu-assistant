# Educational Enquiry Assistant

## features after iter 1 & 2
1. RAG (faiss)
2. LLM using Ollama
3. stateful conversation handling
4. intent detection
5. lead capture
6. explainability + logging

## architecture

User → FastAPI → Intent → State Machine → RAG → LLM → Response

## tech stack
FastAPI, FAISS, Sentence Transformers, Ollama (mistral)

## example

User: What is AI course fee?
→ RAG → Answer

User: I am interested
→ Lead capture flow starts

## to run locally

```bash
pip install -r requirements.txt
```
then 
```bash
python run.py
```

### updating after each iter :))
