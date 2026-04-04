import json
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


with open("facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)

with open("breeds.json", "r", encoding="utf-8") as f:
    breeds = json.load(f)


app = FastAPI(
    title="CatFactsAPI",
    description="Случайные факты о кошках на русском языке",
    version="1.1.1",
    contact={
        "name": "FelineFantasy",
        "email": "mailsalavata5@gmail.com",
        "url": "https://github.com/FelineFantasy/CatFactsAPI",
    }
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def info():
    return {
        "title": "CatFactsAPI",
        "version": "1.1.1",
        "total_facts": len(facts),
        "total_breeds": len(breeds),
        "docs": "https://catfactsapi.onrender.com/docs"
    }


@app.get("/fact")
def random_fact():
    ind = random.randint(0, len(facts) - 1)
    fact = facts[ind]
    return {
        "fact": fact,
        "id": ind,
        "length": len(fact)
    }


@app.get("/facts")
def multiple_facts(limit: int = 1):
    limit = max(1, min(limit, len(facts)))
    selected = random.sample(facts, limit)
    return {
        "facts": selected,
        "count": limit,
        "total": len(facts)
    }


@app.get("/fact/{fact_id}")
def get_fact_by_id(fact_id: int):
    if 0 <= fact_id < len(facts):
        return {
            "fact": facts[fact_id],
            "id": fact_id,
            "length": len(facts[fact_id])
        }
    return {"error": f"ID от 0 до {len(facts) - 1}"}


@app.get("/breed")
def random_breed():
    ind = random.randint(0, len(breeds) - 1)
    breed = breeds[ind]
    return {
        "breed": breed["name"],
        "country": breed["country"],
        "origin": breed["origin"],
        "coat": breed["coat"],
        "pattern": breed["pattern"],
        "id": ind
    }


@app.get("/breeds")
def multiple_breeds(limit: int = 5):
    limit = max(1, min(limit, len(breeds)))
    selected = random.sample(breeds, limit)
    return {
        "breeds": selected,
        "count": limit,
        "total": len(breeds)
    }


@app.get("/breed/{breed_id}")
def get_breed_by_id(breed_id: int):
    if 0 <= breed_id < len(breeds):
        breed = breeds[breed_id]
        return {
            "breed": breed["name"],
            "country": breed["country"],
            "origin": breed["origin"],
            "coat": breed["coat"],
            "pattern": breed["pattern"],
            "id": breed_id
        }
    return {"error": f"ID от 0 до {len(breeds) - 1}"}