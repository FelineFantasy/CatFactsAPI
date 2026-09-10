import sys
import json
import random
from fastapi import FastAPI, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware


try:
    with open("facts.json", "r", encoding="utf-8") as f:
        facts = json.load(f)
except FileNotFoundError:
    print("Ошибка: файл facts.json не найден")
    sys.exit(1)
except json.JSONDecodeError:
    print("Ошибка: файл facts.json имеет неверный формат JSON")
    sys.exit(1)

try:
    with open("breeds.json", "r", encoding="utf-8") as f:
        breeds = json.load(f)
except FileNotFoundError:
    print("Ошибка: файл breeds.json не найден")
    sys.exit(1)
except json.JSONDecodeError:
    print("Ошибка: файл breeds.json имеет неверный формат JSON")
    sys.exit(1)


app = FastAPI(
    title="CatFactsAPI",
    description="Случайные факты о кошках на русском языке",
    version="1.3.0",
    contact={
        "name": "FelineFantasy",
        "email": "mailsalavata5@gmail.com",
        "url": "https://github.com/FelineFantasy/CatFactsAPI",
    },
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def info():
    return {
        "title": "CatFactsAPI",
        "version": "1.3.0",
        "total_facts": len(facts),
        "total_breeds": len(breeds),
        "endpoints": {
            "/": "API info",
            "/fact": "Random fact",
            "/facts": "Multiple facts",
            "/fact/{fact_id}": "Fact by ID",
            "/breed": "Random breed",
            "/breeds": "Multiple breeds",
            "/breed/{breed_id}": "Breed by ID",
        },
        "docs": "https://catfactsapi.onrender.com/docs",
    }


@app.get("/fact")
async def random_fact():
    ind = random.randint(0, len(facts) - 1)
    fact = facts[ind]
    return {"fact": fact, "id": ind, "length": len(fact)}


@app.get("/facts")
async def multiple_facts(limit: int = 1):
    limit = max(1, min(limit, len(facts)))
    selected = random.sample(facts, limit)
    return {"facts": selected, "count": limit, "total": len(facts)}


@app.get("/fact/{fact_id}")
async def get_fact_by_id(fact_id: int):
    if not 0 <= fact_id < len(facts):
        raise HTTPException(
            status_code=404,
            detail=f"Факт с ID={fact_id} не найден. Доступный диапазон: 0..{len(facts) - 1}",
        )
    return {
        "fact": facts[fact_id],
        "id": fact_id,
        "length": len(facts[fact_id]),
    }


@app.get("/breed")
async def random_breed():
    ind = random.randint(0, len(breeds) - 1)
    breed = breeds[ind]
    return {**breed, "id": ind}


@app.get("/breeds")
async def multiple_breeds(limit: int = 5):
    limit = max(1, min(limit, len(breeds)))
    selected = random.sample(breeds, limit)
    return {"breeds": selected, "count": limit, "total": len(breeds)}


@app.get("/breed/{breed_id}")
async def get_breed_by_id(breed_id: int):
    if not 0 <= breed_id < len(breeds):
        raise HTTPException(
            status_code=404,
            detail=f"Порода с ID={breed_id} не найдена. Доступный диапазон: 0..{len(breeds) - 1}",
        )
    breed = breeds[breed_id]
    return {**breed, "id": breed_id}


@app.get("/health")
async def health():
    return {"status": "ok"}
