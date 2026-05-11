markdown

# PAYKX – Deterministic Rail Verification API

**The atomic certainty layer for agentic payments and high-friction corridors.**

PAYKX provides real-time, deterministic **GO / DEGRADED / NO-GO** signals before any capital moves. Built for payment operators and autonomous AI systems that require explainable pre-execution verification on volatile corridors (UK–Nigeria, Ghana, India, and beyond).

Live at: **[api.paykx.co.uk](https://api.paykx.co.uk)**

---

## Key Features

- **Deterministic decisions in < 200ms** – no probabilistic guessing
- **7-signal explainable scoring engine** – fully auditable and regulator-friendly
- **Non-custodial & zero-funds-movement** – we never touch capital
- **Safe Shadow Mode** – read-only testing with full audit logs
- **Live FX integration** – real-time GBP/NGN rates (VertoFX + cache)
- **Production-grade** – rate limiting, API key auth, structured logging

---

## Core Problem We Solve

High-friction corridors suffer from an 8–12% "Shadow Tax" — failed or delayed transactions that trap liquidity and create massive manual reconciliation overhead. Legacy systems discover problems *after* capital has moved. PAYKX prevents that.

---

## The 7 Signals (Explainable Scoring)

Our engine evaluates every verification request across seven real-time signals:

1. **Balance & Liquidity**  
2. **Operation & Status**  
3. **Network & Latency**  
4. **Historical Failure Patterns**  
5. **CoP Override Behaviour**  
6. **FX Volatility (live GBP/NGN)**  
7. **Behavioral / Fraud-Aware Flags**

Each signal is weighted, explainable, and logged for full auditability.

---

## Architecture Overview

- **FastAPI** backend (Python)
- **PostgreSQL + Redis** for persistence and caching
- **TigerBeetle-inspired** deterministic logic
- **VertoFX** live rate integration with 3-minute cache
- **Fail-open design** – never blocks unless explicitly configured

---

## API Endpoints (v1)

| Method | Endpoint                  | Description                          |
|--------|---------------------------|--------------------------------------|
| `POST` | `/api/v1/verify`          | Main verification endpoint           |
| `GET`  | `/api/v1/health`          | Health check + version               |
| `GET`  | `/api/v1/verto/rates`     | Live GBP/NGN rate (cached)           |
| `POST` | `/api/v1/demo-verify`     | Public demo endpoint                 |

Full OpenAPI spec available at `/docs` when running locally.

**Example request (cURL)**

```bash
curl -X POST https://api.paykx.co.uk/api/v1/verify \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "corridor": "GB-NG",
    "amount": 1500,
    "currency": "GBP",
    "operator": "GTBank"
  }'

Compliance & SecurityFCA Digital Sandbox – Full-length testing live (May 2026)
SEIS Advance Assurance received
GDPR & UK Data Protection compliant
Non-custodial by design
Full audit logging for every decision

Getting Started (Local Development)bash

git clone https://github.com/taseenrayed-a11y/api-paykx-.git
cd api-paykx-
pip install -r requirements.txt
uvicorn main:app --reload

Open http://127.0.0.1:8000/docs for interactive Swagger UI.StatusLive Production: api.paykx.co.uk
FCA Digital Sandbox: Full-length testing active
First corridor: UK–Nigeria (others in pipeline)
Current focus: Operator Shadow Diagnostics

ContactFounder & CEO: Taseen Rayed
Email: taseenrayed@paykx.co.uk
Website: paykx.co.uk
API: api.paykx.co.uk

Built in London. Designed for global agentic finance.

