# 🐱 CatFactsAPI

API для получения случайных фактов и информации о породах кошек на русском языке.

## 📋 Описание

CatFactsAPI — это простой и лёгкий REST API, построенный на **FastAPI**, который возвращает случайные факты о кошках и информацию о породах. Идеально подходит для учебных проектов, тестовых приложений или просто для развлечения.

## 🚀 Возможности

- ✅ Случайные факты о кошках
- ✅ **100+ уникальных фактов** в базе
- ✅ Информация о породах кошек
- ✅ Получение факта или породы по ID
- ✅ Информация о длине факта
- ✅ Автоматическая документация через Swagger UI
- ✅ **API на русском языке**

## 📦 Установка

### Требования

- Python 3.8+
- pip

### Шаги установки

1. Клонируйте репозиторий:
```bash
git clone https://github.com/FelineFantasy/CatFactsAPI
cd CatFactsAPI
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## 🏃 Запуск

### Локальный запуск

Запустите сервер с помощью Uvicorn:

```bash
uvicorn main:app --reload
```

Сервер будет доступен по адресу: **http://localhost:8000**

### Онлайн версия

API уже развёрнут и доступен по адресу: **https://catfactsapi.onrender.com**

## 📡 API Endpoints

### Факты о кошках

| Метод | Эндпоинт | Описание |
|-------|----------|-----------|
| GET | `/` | Информация об API |
| GET | `/fact` | Случайный факт |
| GET | `/facts?limit=5` | Несколько случайных фактов |
| GET | `/fact/{id}` | Факт по ID (0–99) |

### Породы кошек

| Метод | Эндпоинт | Описание |
|-------|----------|-----------|
| GET | `/breed` | Случайная порода |
| GET | `/breeds?limit=5` | Несколько пород |
| GET | `/breed/{id}` | Порода по ID (0–9) |

## 📖 Документация

Интерактивная документация доступна по адресу:

- **Swagger UI:** https://catfactsapi.onrender.com/docs
- **ReDoc:** https://catfactsapi.onrender.com/redoc

При локальном запуске:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🧪 Примеры использования

### cURL
```bash
# Случайный факт
curl https://catfactsapi.onrender.com/fact

# Случайная порода
curl https://catfactsapi.onrender.com/breed

# 3 случайных факта
curl https://catfactsapi.onrender.com/facts?limit=3

# Факт по ID
curl https://catfactsapi.onrender.com/fact/42

# Порода по ID
curl https://catfactsapi.onrender.com/breed/5
```

### Python
```python
import requests

# Случайный факт
response = requests.get("https://catfactsapi.onrender.com/fact")
data = response.json()
print(data["fact"])

# Случайная порода
response = requests.get("https://catfactsapi.onrender.com/breed")
data = response.json()
print(data["breed"], data["country"])
```

### JavaScript (Fetch API)
```javascript
// Случайный факт
fetch('https://catfactsapi.onrender.com/fact')
  .then(response => response.json())
  .then(data => console.log(data.fact));

// Случайная порода
fetch('https://catfactsapi.onrender.com/breed')
  .then(response => response.json())
  .then(data => console.log(data.breed, data.country));
```

## 📁 Структура проекта

```
CatFactsAPI/
├── main.py           # Основной файл приложения
├── facts.json        # База фактов о кошках (100+)
├── breeds.json       # База пород кошек (10+)
├── requirements.txt  # Зависимости проекта
└── README.md         # Документация
```

## 🛠 Технологии

- **FastAPI** — современный веб-фреймворк для создания API
- **Uvicorn** — ASGI сервер
- **Render** — хостинг (живая версия)

## 📝 Лицензия

MIT

## 🔗 Ссылки

- **API**: https://catfactsapi.onrender.com
- **Документация**: https://catfactsapi.onrender.com/docs
- **GitHub**: https://github.com/FelineFantasy/CatFactsAPI

---

Сделано с ❤️ для любителей кошек
