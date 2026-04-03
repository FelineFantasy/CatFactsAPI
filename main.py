import json
import random
import time
from fastapi import FastAPI, Request

with open("facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)

app = FastAPI(
    title="CatFactsAPI",
    description="Случайные факты о кошках",
    version="1.0.0",
)

@app.get("/")
def info():
    return {
        "title": "CatFactsAPI",
        "version": "1.0.0",
    }

@app.get("/fact")
def root(request: Request):
    client_ip = request.client.host
    print(f"[Факт запрошен] - IP: {client_ip} - Время: {time.strftime('%H:%M:%S')}")

    fact = random.choice(facts)
    return {
        "fact": fact,
        "length": len(fact),
    }