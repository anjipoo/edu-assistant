# Educational Enquiry Assistant

## features after iter 1 & 2
1. RAG (faiss)
2. LLM using Ollama
3. stateful conversation handling
4. intent detection
5. lead capture
6. explainability + logging

## features after iter 3
1. lead scoring system
2. user behavior tracking (fees / details / interest)
3. lead classification (HOT 🔥 / WARM / COLD)

## features after iter 4
1. hybrid intent detection (rule-based + LLM fallback)
2. better handling of natural language queries

## features after iter 5
1. conversation memory
2. context-aware responses (multi-turn understanding)
3. history-based prompt injection

## features after iter 6
1. proactive follow-up generation

## architecture

User → FastAPI → Intent → State Machine → RAG → LLM → Response

## tech stack
FastAPI, FAISS, Sentence Transformers, Ollama (mistral)

## example

User: Tell me about AI course

→ RAG → Answer


User: What is the fee?

→ Uses memory → AI course fee


User: I am interested

→ Lead capture flow starts


User: Sam

User: AI

User: xxxxxxxxxx

→ Lead stored (HOT 🔥)

→ Follow-up message generated

## to run locally

```bash
pip install -r requirements.txt
```
then 
```bash
python run.py
```

### updating after each iter :))
