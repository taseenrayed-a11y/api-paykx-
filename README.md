# PAYKX Rail Verification API

**Atomic Certainty Layer for High-Friction Corridors**

PAYKX is a non-custodial infrastructure layer that verifies payment rail health in real time before funds are committed. If the corridor is unstable, it blocks the transaction — preventing trapped capital.

## Key Features
- Deterministic GO/NO-GO decisions in <50ms
- Fully explainable agentic probes (behavioral, network, historical)
- Safe shadow mode for partner testing
- Complete audit logging
- Rate limiting + API key authentication

## Live Demo
https://paykx-api-taseenrayed.replit.app

## How to Run Locally
```bash
git clone https://github.com/taseenrayed-a11y/api-paykx-.git
cd api-paykx-
pip install -r requirements.txt
uvicorn main:app --reload
https://documenter.getpostman.com/view/52813753/2sBXcKBHke#d83b04c4-1f2f-4c40-9dc6-4c9c2cba49e1
