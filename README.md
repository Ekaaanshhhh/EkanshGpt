# EkanshGPT 🤖

A RAG-powered AI chatbot for Ekansh's portfolio website. Ask it questions about projects, experience, skills, achievements, and more — all powered by your own data.

## Architecture

```
Frontend  →  Next.js portfolio website
Backend   →  Python FastAPI server
VectorDB  →  ChromaDB
LLM       →  Google Gemini (RAG, not fine-tuned)
```

## Backend Setup

### Prerequisites

- Python 3.11+
- A [Gemini API key](https://aistudio.google.com/app/apikey)

### Quick Start

```bash
# 1. Navigate to the backend
cd backend

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up your environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# 6. Run the server
uvicorn app.main:app --reload --port 8000
```

### Verify

- **Health check:** [http://localhost:8000/api/health](http://localhost:8000/api/health)
- **API Docs (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **API Docs (ReDoc):** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── config.py            # Environment configuration
│   ├── routers/             # HTTP endpoint definitions
│   │   └── ingest.py        # Document upload endpoint
│   ├── services/            # Business logic
│   │   ├── ingestion_service.py  # Pipeline orchestrator
│   │   ├── file_parser.py   # PDF/TXT/MD text extraction
│   │   ├── chunker.py       # Text chunking
│   │   └── vector_store.py  # ChromaDB + embeddings
│   ├── models/
│   │   └── schemas.py       # Pydantic data models
│   └── utils/
│       └── logger.py        # Logging configuration
├── data/chroma_db/          # Vector database storage
├── uploads/                 # Temporary file uploads
├── requirements.txt
├── .env.example
└── .gitignore
```

## Document Taxonomy

Documents are categorized for structured retrieval:

| Category | Description |
|---|---|
| `resume` | CV, resume documents |
| `project` | Project descriptions (ReelOps, MediSaar, etc.) |
| `achievement` | Awards, hackathon wins, certifications |
| `experience` | Work experience, internships |
| `education` | Degrees, courses, academic records |
| `blog` | Blog posts, articles, write-ups |

## License

Private — All rights reserved.
