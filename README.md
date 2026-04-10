# 🐱 CatFactsAPI

API for getting random facts and information about cat breeds in English.

## 📋 Description

CatFactsAPI is a simple and lightweight REST API built with **FastAPI** that returns random facts about cats and breed information. Perfect for educational projects, test applications, or just for fun.

## 🚀 Features

- ✅ Random cat facts
- ✅ **100+ unique facts** in the database
- ✅ Cat breed information
- ✅ Get fact or breed by ID
- ✅ Fact length information
- ✅ Automatic documentation via Swagger UI
- ✅ **English-language API**

## 📦 Installation

### Requirements

- Python 3.8+
- pip

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/FelineFantasy/CatFactsAPI
cd CatFactsAPI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🏃 Running

### Local Run

Start the server using Uvicorn:

```bash
uvicorn main:app --reload
```

The server will be available at: **http://localhost:8000**

### Online Version

The API is already deployed and available at: **https://catfactsapi.onrender.com**

## 📡 API Endpoints

### Cat Facts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/fact` | Random fact |
| GET | `/facts?limit=5` | Multiple random facts |
| GET | `/fact/{id}` | Fact by ID (0–99) |

### Cat Breeds

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/breed` | Random breed |
| GET | `/breeds?limit=5` | Multiple breeds |
| GET | `/breed/{id}` | Breed by ID (0–9) |

## 📖 Documentation

Interactive documentation is available at:

- **Swagger UI:** https://catfactsapi.onrender.com/docs
- **ReDoc:** https://catfactsapi.onrender.com/redoc

When running locally:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🧪 Usage Examples

### cURL
```bash
# Random fact
curl https://catfactsapi.onrender.com/fact

# Random breed
curl https://catfactsapi.onrender.com/breed

# 3 random facts
curl https://catfactsapi.onrender.com/facts?limit=3

# Fact by ID
curl https://catfactsapi.onrender.com/fact/42

# Breed by ID
curl https://catfactsapi.onrender.com/breed/5
```

### Python
```python
import requests

# Random fact
response = requests.get("https://catfactsapi.onrender.com/fact")
data = response.json()
print(data["fact"])

# Random breed
response = requests.get("https://catfactsapi.onrender.com/breed")
data = response.json()
print(data["breed"], data["country"])
```

### JavaScript (Fetch API)
```javascript
// Random fact
fetch('https://catfactsapi.onrender.com/fact')
  .then(response => response.json())
  .then(data => console.log(data.fact));

// Random breed
fetch('https://catfactsapi.onrender.com/breed')
  .then(response => response.json())
  .then(data => console.log(data.breed, data.country));
```

## 📁 Project Structure

```
CatFactsAPI/
├── main.py           # Main application file
├── facts.json        # Cat facts database (100+)
├── breeds.json       # Cat breeds database (10+)
├── requirements.txt  # Project dependencies
└── README.md         # Documentation
```

## 🛠 Technologies

- **FastAPI** — Modern web framework for building APIs
- **Uvicorn** — ASGI server
- **Render** — Hosting (live version)

## 📝 License

MIT

## 🔗 Links

- **API**: https://catfactsapi.onrender.com
- **Documentation**: https://catfactsapi.onrender.com/docs
- **GitHub**: https://github.com/FelineFantasy/CatFactsAPI

---

Made with ❤️ for cat lovers
