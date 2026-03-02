# api-paykx-
api paykx
# PAYKX Rail Verification API

## What is PAYKX?
PAYKX is a non-custodial certainty layer that verifies payment rail health in real time for high-friction corridors (starting with UK–Nigeria). It blocks unsafe transactions before funds move — preventing trapped liquidity.

## Key Features
- Deterministic GO/NO-GO decisions (<50ms)
- Explainable probes (behavioral, network, historical)
- Shadow mode for safe partner testing
- Full audit logging
- Rate limiting & API key auth

## How to Run Locally
1. Clone repo: `git clone https://github.com/taseenrayed/paykx-api.git`
2. Install deps: `pip install -r requirements.txt`
3. Run: `uvicorn main:app --reload`
4. Visit: http://localhost:8000/docs (Swagger UI)

## Live Demo
https://paykx-api-taseenrayed.replit.app  
(Shadow mode demo — use mode=shadow)

## Current Status (March 2026)
- Pre-pilot, pre-revenue
- 200+ simulation cycles
- £1.7M simulated harm prevented
- SEIS Advance Assurance submitted
- Built with FastAPI + SQLite for fast iteration and auditability. Shadow mode enables safe partner testing.
  

Contact: taseenrayed@paykx.co.uk
