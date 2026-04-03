# 🐱 CatFactsAPI

API для получения случайных фактов о кошках на русском языке.

## 📋 Описание

CatFactsAPI — это простой и лёгкий REST API, построенный на **FastAPI**, который возвращает случайные факты о кошках. Идеально подходит для учебных проектов, тестовых приложений или просто для развлечения.

## 🚀 Возможности

- ✅ Случайные факты о кошках
- ✅ 49 уникальных фактов в базе
- ✅ Информация о длине факта
- ✅ Логирование запросов с IP-адресом и временем
- ✅ Автоматическая документация через Swagger UI

## 📦 Установка

### Требования

- Python 3.8+
- pip

### Шаги установки

1. Клонируйте репозиторий или скопируйте файлы проекта:
```bash
cd CatFactsAPI
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## 🏃 Запуск

Запустите сервер с помощью Uvicorn:

```bash
uvicorn main:app --reload
```

Сервер будет доступен по адресу: **http://localhost:8000**

## 📡 API Endpoints

### `GET /` — Информация о API

Возвращает название и версию API.

**Ответ:**
```json
{
  "title": "CatFactsAPI",
  "version": "1.0.0"
}
```

### `GET /fact` — Случайный факт о кошках

Возвращает случайный факт из базы данных.

**Ответ:**
```json
{
  "fact": "У кошек около 230 костей - на 24 больше, чем у человека.",
  "length": 58
}
```

## 📖 Документация

После запуска сервера автоматически генерируется интерактивная документация:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🧪 Примеры использования

### cURL
```bash
curl http://localhost:8000/fact
```

### Python
```python
import requests

response = requests.get("http://localhost:8000/fact")
data = response.json()
print(data["fact"])
```

### JavaScript (Fetch API)
```javascript
fetch('http://localhost:8000/fact')
  .then(response => response.json())
  .then(data => console.log(data.fact));
```

## 📁 Структура проекта

```
CatFactsAPI/
├── main.py           # Основной файл приложения
├── facts.json        # База фактов о кошках
├── requirements.txt  # Зависимости проекта
└── README.md         # Документация
```

## 🛠 Технологии

- **FastAPI** — современный веб-фреймворк для создания API
- **Uvicorn** — ASGI сервер

## 📝 Лицензия

MIT

---

Сделано с ❤️ для любителей кошек
