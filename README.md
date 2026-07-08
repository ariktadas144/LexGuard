# LexGuard

**AI-Powered Legal Document Analyzer**

LexGuard is an intelligent legal assistance platform that simplifies complex legal agreements into clear, human-readable insights. It helps users identify hidden risks, one-sided clauses, and unfair liabilities in contracts — and provides AI-generated negotiation suggestions — before they sign.

---

## Table of Contents

- [Problem Statement](#problem-statement)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Target KPIs](#target-kpis)
- [Datasets & Open Models Used](#datasets--open-models-used)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Real-World Applications](#real-world-applications)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Problem Statement

Legal and contractual documents — employment contracts, rental agreements, NDAs, internship offers, freelance contracts, and service agreements — are often written in dense legal language that's hard for non-lawyers to interpret. Traditional legal review is expensive, slow, and inaccessible for individuals and small businesses.

LexGuard solves this by using AI to extract, classify, and evaluate clauses automatically, producing both a **detailed clause-by-clause risk analysis** and a **simplified overall safety overview**.

---

## Key Features

- **Secure Authentication** — JWT / Firebase Auth based login & signup
- **Multi-Format Upload** — supports PDF, JPG, and PNG documents (OCR for scanned files)
- **Clause Extraction & Classification** — automatically detects and categorizes clauses (Termination, Payment, Liability, Confidentiality, IP, Non-Compete, Arbitration, Penalties)
- **Clause-Level Risk Scoring** — each clause gets a risk score, plain-language explanation, and suggested safer alternative
- **Overall Document Safety Score** — a single 0–10 score with classification: **Safe / Needs Review / High Risk**
- **AI Negotiation Assistant** — flags one-sided terms and suggests specific negotiation points
- **Document History & Comparison** — searchable dashboard of past analyses
- **Final Risk Summary Report** — exportable structured report with a signing recommendation

---

## System Architecture

```
Frontend (React)
      ↓
FastAPI Gateway
      ↓
Authentication Layer
      ↓
Document Upload Service
      ↓
Celery Queue (Redis)
      ↓
OCR + Parsing Pipeline
      ↓
Clause Extraction Engine
      ↓
Embedding Generation
      ↓
MongoDB + pgvector Storage
      ↓
LangGraph AI Agents
      ↓
Risk Analysis + Negotiation Suggestions
      ↓
JSON Report Generator
      ↓
Frontend Dashboard
```

**Flow summary:**
1. **Ingestion** — Next.js/React UI → FastAPI → Celery Worker (Redis queue) handles heavy OCR/PDF extraction asynchronously.
2. **Analysis** — Document chunks are embedded and stored in pgvector / MongoDB Atlas Vector Search.
3. **Reasoning** — LangGraph agents (powered by Claude 3.5 Sonnet) run hybrid search (BM25 + semantic) to isolate and evaluate risky clauses.
4. **Delivery** — A structured JSON report is streamed back to the frontend dashboard.

---

## Tech Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React (Vite), Tailwind CSS, Shadcn/ui |
| **Backend & APIs** | Python, FastAPI, Docker |
| **Async Workers** | Celery, Redis |
| **AI Engine** | Anthropic Claude 3.5 Sonnet, LangGraph, LlamaIndex |
| **Database & Search** | MongoDB Atlas (Vector Search + Atlas Search), PostgreSQL (pgvector) |
| **OCR** | Tesseract OCR, EasyOCR |
| **PDF Parsing** | PyMuPDF, PDFPlumber |
| **NLP / ML** | Legal-BERT, Sentence-BERT, Hugging Face Transformers, spaCy, Scikit-learn |
| **Similarity Search** | FAISS / ChromaDB |
| **Storage** | AWS S3 / Firebase Storage |
| **Authentication** | JWT / Firebase Auth |

---

## Project Structure

```
frontend/                              # React + Vite + Tailwind + Shadcn
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── ui/                        # shadcn primitives
│   │   ├── upload/                    # multi-format upload UI
│   │   ├── clause/                    # clause highlight + explanation cards
│   │   ├── dashboard/                 # risk dashboards, charts
│   │   ├── report/                    # final report/negotiation view
│   │   └── layout/                    # navbar, sidebar, shell
│   ├── pages/
│   │   ├── Login.tsx
│   │   ├── Signup.tsx
│   │   ├── Dashboard.tsx
│   │   ├── DocumentUpload.tsx
│   │   ├── ClauseAnalysis.tsx         # detailed mode
│   │   ├── DocumentOverview.tsx       # simplified mode
│   │   ├── History.tsx
│   │   └── ReportView.tsx
│   ├── hooks/
│   ├── lib/
│   ├── store/
│   ├── types/
│   ├── App.tsx
│   └── main.tsx
├── tailwind.config.ts
├── vite.config.ts
└── package.json

ml_engine/                             # AI/ML analysis engine
├── ingestion/
│   ├── ocr/
│   ├── pdf_parser/
│   └── document_loader.py
├── clause_extraction/
│   ├── segmenter.py
│   ├── classifier.py                  # Legal-BERT fine-tuned
│   ├── labels.py
│   └── training/
├── embeddings/
│   ├── sentence_bert_encoder.py
│   ├── chunker.py
│   └── vector_store.py
├── risk_analysis/
│   ├── risk_scorer.py
│   ├── rules/
│   └── consistency_checker.py
├── agents/                            # LangGraph orchestration
│   ├── graph_builder.py
│   ├── nodes/
│   └── prompts/
├── llm/
│   ├── claude_client.py
│   └── llamaindex_index.py
├── evaluation/
├── models/
├── config.py
├── requirements.txt
└── main_pipeline.py

backend/                                # FastAPI gateway, auth, DB models (WIP)
docker-compose.yml
.gitignore
README.md
```

---

## Target KPIs

| Metric | Target | Baseline Benchmark |
|---|---|---|
| Clause Classification Accuracy | ≥ 90% | 80–85% (traditional NLP) |
| OCR Text Extraction Accuracy | ≥ 95% | 85–90% (standard OCR) |
| Risk Prediction Consistency | ≥ 85% | Rule-based legal analyzers |
| Clause Detection Accuracy | ≥ 90% | Existing document parsers |
| AI Summary Relevance | ≥ 85% user satisfaction | Generic summarization models |
| Document Processing Time | < 30 sec/document | Manual legal review |
| User Understanding Improvement | ≥ 70% positive feedback | No-AI baseline |
| Negotiation Suggestion Quality | ≥ 80% relevance score | Static legal templates |

---

## Datasets & Open Models Used

**Language Models**
- Anthropic Claude 3.5 Sonnet — clause explanation, risk summarization, negotiation suggestions
- Legal-BERT — legal text classification & embeddings
- Sentence-BERT — semantic similarity & clause comparison

**Datasets**
- CUAD (Contract Understanding Atticus Dataset)
- LEDGAR Dataset
- CaseHOLD Dataset
- ContractNLI
- LexGLUE Benchmark

---

## Getting Started

### Prerequisites
- Node.js ≥ 18
- Python ≥ 3.10
- Docker & Docker Compose
- Redis
- MongoDB Atlas account (or local MongoDB)
- PostgreSQL with `pgvector` extension
- Anthropic API key

### 1. Clone the repository
```bash
git clone https://github.com/ariktadas144/LexGuard.git
cd LexGuard
```

### 2. Frontend setup
```bash
cd frontend
npm install
npm run dev
```

### 3. ML Engine / Backend setup
```bash
cd ml_engine
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Start services with Docker
```bash
docker-compose up --build
```

---

## Environment Variables

Create a `.env` file in both `frontend/` and `ml_engine/` (or root, depending on your setup):

```env
# AI
ANTHROPIC_API_KEY=your_key_here

# Database
MONGODB_URI=your_mongodb_atlas_uri
POSTGRES_URL=your_postgres_connection_string

# Redis / Celery
REDIS_URL=redis://localhost:6379

# Auth
JWT_SECRET=your_jwt_secret
FIREBASE_CONFIG=your_firebase_config

# Storage
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
S3_BUCKET_NAME=your_bucket
```

> Never commit `.env` files. They're excluded via `.gitignore`.

---

## Real-World Applications

LexGuard can be used to analyze:
- Employment contracts & internship offers
- Rental agreements
- Freelance & vendor agreements
- NDAs
- Service contracts
- Terms & Conditions / Privacy Policies
- Partnership agreements

---

## Roadmap

- [ ] Core OCR + clause extraction pipeline
- [ ] Legal-BERT clause classifier fine-tuning
- [ ] LangGraph risk-analysis agent workflow
- [ ] Negotiation suggestion engine
- [ ] Document history & comparison dashboard
- [ ] Multi-language document support
- [ ] Downloadable PDF risk reports

---

## Contributing

Contributions are welcome. Please open an issue to discuss proposed changes before submitting a pull request.

```bash
git checkout -b feature/your-feature-name
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
```

---

## License

This project is licensed under the MIT License.

---

**Built by [Arikta Das](https://github.com/ariktadas144)**
