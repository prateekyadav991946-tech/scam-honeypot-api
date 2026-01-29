from fastapi import FastAPI
from detector import detect_scam
from responder import generate_reply
from extractor import extract_intel

app = FastAPI(title="Scam Honeypot API")

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/message")
def message(data: dict):
    text = data.get("message", "")
    analysis = detect_scam(text)
    reply = generate_reply(analysis)
    intelligence = extract_intel(text)

    return {
        "input_message": text,
        "analysis": analysis,
        "auto_reply": reply,
        "extracted_intelligence": intelligence
    }

