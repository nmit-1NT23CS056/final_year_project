# Intelligent Career Path Advisory Agent for Senior IT Professionals

> Major Capstone Project — Phase 1 | NMIT, VTU | Academic Year 2025–26

**Team:**
- Deepanshu Bisht (1NT23CS056)
- Divya S Karki (1NT23CS067)

**Guide:** Dr. Krishna Rao Venkatesh, Professor, Dept. of CSE, NMIT

---

## Problem Statement

Existing career platforms like LinkedIn, Naukri, and Glassdoor are optimized for early-career job matching and do not address the complex advisory needs of senior IT professionals. A Senior Engineer with 5+ years of experience navigating transitions into Engineering Management, Technical Architecture, or CTO roles requires personalized, explainable guidance — not keyword-based job recommendations.

This project builds an AI-powered career advisory agent that combines five-dimensional psychometric profiling (including Emotional Intelligence), LLM-based reasoning, and Retrieval-Augmented Generation to deliver personalized career path recommendations for experienced IT professionals.

---

## Functional Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| FR1 | Five-dimensional assessment form (Technical Skills, Soft Skills, Career Motivators, Personality Traits, EQ) with structured profile storage | ✅ Complete |
| FR2 | LLM-powered career path recommendations — at least 3 personalized senior-level paths including one leadership transition | ✅ Complete |
| FR3 | Skill gap analysis with prioritized learning roadmap against senior role benchmarks | ✅ Complete — implemented via ChromaDB RAG pipeline (14 role/level benchmark docs, top-3 retrieval, gap identified per recommendation) |
| FR4 | PDF resume upload with NLP-based parsing, auto-populating the five-dimensional profile | ✅ Complete — implemented via pdfplumber + Gemini structured extraction |
| FR5 | Live senior-level job postings matched to each recommendation via real-time job listings API | ⬜ Planned (Phase B) |
| FR6 | Career transition classification (lateral/upward/pivot) + 0–100 readiness score vs peer transition profiles | ⬜ Planned (Phase B) |
| FR7 | Mentor matching via cosine similarity over vector-encoded transition profiles | ⬜ Planned (Phase B) |
| FR8 | SMART goal tracking with milestone persistence and completion tracking | ⬜ Planned (Phase B) |

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend API | Python 3.11, FastAPI |
| Database | SQLite + SQLAlchemy |
| Vector Database | ChromaDB (skill-benchmark knowledge base + semantic retrieval) |
| Orchestration | LangGraph (multi-node recommendation pipeline) |
| LLM | Google Gemini 2.5 Flash (via `google-genai`) |
| Resume Parsing | pdfplumber (PDF text extraction) |
| Frontend | React 19 + Vite + Tailwind CSS |
| Routing | React Router DOM |
| Notifications | React Hot Toast |
| HTTP Client | Axios |
| Version Control | Git + GitHub |

---

## System Architecture

```
User (Browser)
     │
     ▼
React Frontend (localhost:5173)
     │  Axios HTTP calls
     ▼
FastAPI Backend (localhost:8000)
     ├── POST /api/profile          → Save 5-dimensional profile → SQLite
     ├── GET  /api/profile/{email}  → Fetch profile
     ├── POST /api/resume/parse     → pdfplumber extracts PDF text → Gemini extracts
     │                                 structured fields (skills, role, traits) → JSON
     └── POST /api/recommend/{email} → LangGraph pipeline:
             │
             ├─ 1. Profile Analyzer   → builds retrieval query from profile
             ├─ 2. Retriever          → searches ChromaDB for top-3 relevant
             │                           skill-benchmark documents
             ├─ 3. Recommendation     → Gemini 2.5 Flash generates 3 career
             │      Generator            paths, grounded in retrieved docs
             └─ 4. Validator          → checks output format before returning
     │
     ▼
SQLite Database (profiles.db)  +  ChromaDB (chroma_data/)  +  Google Gemini 2.5 Flash API
```

---

## Project Structure

```
final_year_project/
├── backend/
│   ├── main.py                  # FastAPI app entry point, CORS config
│   ├── database.py              # SQLAlchemy engine, session, Base
│   ├── models.py                # UserProfile SQLAlchemy model
│   ├── knowledge_base.py        # 14 role/level skill-benchmark documents
│   ├── vector_store.py          # ChromaDB client, load + search functions
│   ├── load_kb.py               # One-time script to load knowledge base into ChromaDB
│   ├── requirements.txt         # Python dependencies
│   ├── graph/
│   │   ├── state.py             # Shared state schema (RecommendationState)
│   │   ├── nodes.py             # 4 pipeline nodes (analyzer, retriever, generator, validator)
│   │   └── graph.py             # LangGraph StateGraph wiring
│   └── routes/
│       ├── profile.py           # POST /api/profile, GET /api/profile/{email}
│       ├── resume.py            # POST /api/resume/parse — pdfplumber + Gemini extraction
│       └── recommend.py         # POST /api/recommend/{email} — invokes LangGraph pipeline
├── frontend/
│   └── src/
│       ├── App.jsx              # BrowserRouter + Routes
│       ├── pages/
│       │   ├── AssessmentPage.jsx   # 5-dimensional assessment form + resume upload
│       │   └── RecommendPage.jsx    # Career recommendations display
│       └── utils/
│           └── axios.js         # Axios instance (baseURL: localhost:8000)
├── .gitignore
├── Intelligent_Career_Path_Advisory_Agent_Synopsis.pdf
└── README.md
```

---

## Setup Instructions

### Prerequisites
- Python 3.11+
- Node.js 18+
- A Google Gemini API key from [aistudio.google.com](https://aistudio.google.com/apikey)

### Backend Setup

```bash
# 1. Clone the repository
git clone https://github.com/nmit-1NT23CS056/final_year_project
cd final_year_project

# 2. Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r backend/requirements.txt

# 4. Create .env file inside backend/
# backend/.env
GEMINI_API_KEY=your_gemini_api_key_here

# 5. Load the skill-benchmark knowledge base into ChromaDB (one-time step)
python -m backend.load_kb

# 6. Run the backend server
uvicorn backend.main:app --reload
```

Backend runs at: `http://localhost:8000`
API docs available at: `http://localhost:8000/docs`

### Frontend Setup

```bash
# In a new terminal
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## How to Use

1. Open `http://localhost:5173`
2. (Optional) Upload a resume PDF and click **Parse Resume** to auto-fill fields
3. Fill in the 5-dimensional assessment form:
   - Basic Information (name, email, years of experience, current role)
   - Dimension 1: Technical Skills
   - Dimension 2: Soft Skills
   - Dimension 3: Career Motivators
   - Dimension 4: Personality Traits
   - Dimension 5: Emotional Intelligence (EQ sliders 1-10)
4. Click **Submit Profile** — profile is saved to SQLite
5. Click **Get My Recommendations →**
6. View 3 personalized AI-generated career path recommendations, each grounded in retrieved skill-benchmark documents and including an explicit **Skill Gap Identified** section

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/profile` | Create a new 5-dimensional user profile |
| GET | `/api/profile/{email}` | Fetch a saved profile by email |
| POST | `/api/resume/parse` | Extract structured profile fields from an uploaded PDF resume |
| POST | `/api/recommend/{email}` | Run the LangGraph pipeline to generate RAG-grounded career recommendations |

---

## Key Design Decisions

- **SQLite** chosen over Firebase for prototype simplicity — no external service dependency
- **Gemini 2.5 Flash** chosen for its strong reasoning capability and free-tier availability
- **ChromaDB** chosen for the RAG pipeline — a lightweight, local-first vector database that needs no separate server, storing a 14-document skill-benchmark knowledge base (role/level pairs across Backend, Frontend, Full-Stack, Data/ML, DevOps, Engineering Management, Product, and QA tracks) with built-in embeddings for semantic retrieval
- **LangGraph** chosen to structure the recommendation flow as an explicit 4-node pipeline (Profile Analyzer → Retriever → Recommendation Generator → Validator) rather than one monolithic prompt — this isolates each responsibility, making the flow easier to reason about, debug, and extend
- **pdfplumber** chosen for resume parsing — extracts raw text from PDF resumes, which Gemini then structures into profile fields, reducing manual form-filling
- **CORS** configured to allow frontend-backend communication on localhost
- **Modular routing** — each feature has its own route file for clean separation

---

## References

1. Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," NeurIPS, 2020. https://arxiv.org/abs/2005.11401
2. Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models," ICLR, 2023. https://arxiv.org/abs/2210.03629
3. Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," NeurIPS, 2022. https://arxiv.org/abs/2201.11903
4. Wang et al., "A Survey on Large Language Model based Autonomous Agents," Frontiers of Computer Science, 2024. https://arxiv.org/abs/2308.11432
5. Ravuru et al., "Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG," arXiv, 2025. https://arxiv.org/abs/2501.09136
6. Park et al., "Personality-Aware Career Recommendation Using Big Five Model," Journal of Information Science, 2021.
