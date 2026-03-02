from fastapi import FastAPI, Depends, Header, HTTPException, Query
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from datetime import datetime
import statistics
import random
import json
import requests
from pydantic import BaseModel

from db.database import SessionLocal, engine, Base
from db.models import Verification, AccessRequest
from core.config import settings
from services.circuit_breaker import (
    is_in_cooldown,
    activate_cooldown
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PAYKX Rail Verification API",
    version="1.0.1",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()

class VerifyRequest(BaseModel):
    corridor: str

class AccessRequest(BaseModel):
    name: str
    email: str
    reason: str
    recaptcha_token: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def require_api_key(authorization: str = Depends(security)):
    if authorization.credentials not in settings.API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key.")
    return authorization.credentials

# ─────────────────────────────────────────
# CLEAN ROOT WELCOME PAGE
# ─────────────────────────────────────────
@app.get("/")
def root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PAYKX API • Demo</title>
        <style>
            body { font-family: 'Inter', system-ui, sans-serif; background: #020617; color: #f1f5f9; text-align: center; padding: 60px 20px; margin: 0; }
            .banner { background: #f59e0b; color: #1e2937; padding: 14px; font-weight: bold; position: fixed; top: 0; left: 0; width: 100%; z-index: 100; }
            h1 { font-size: 2.8rem; margin: 80px 0 10px; }
            p { font-size: 1.15rem; max-width: 620px; margin: 0 auto 30px; color: #cbd5e1; }
            .links a { display: inline-block; margin: 12px; padding: 14px 28px; background: #0ea5e9; color: white; text-decoration: none; border-radius: 8px; font-weight: 600; }
            .links a:hover { background: #0284c8; }
        </style>
    </head>
    <body>
        <div class="banner">
            ⚠️ DEMO / SHADOW MODE — All data is simulated. Not for live or production use.
        </div>
        
        <h1>PAYKX</h1>
        <p><strong>Rail Verification API</strong><br>
        Deterministic certainty layer for high-friction corridors</p>
        
        <div class="links">
            <a href="/api/health">Health Check</a>
            <a href="/docs">API Documentation</a>
            <a href="/api/v1/request-access">Request Technical Access</a>
        </div>
        
        <p style="margin-top: 60px; font-size: 0.95rem; color: #64748b;">
            Built for partners & investors • March 2026
        </p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# ─────────────────────────────────────────
# HEALTH CHECK
# ─────────────────────────────────────────
@app.get("/api/health")
def health_check(db: Session = Depends(get_db)):
    total = db.query(Verification).count()
    return {
        "status": "healthy",
        "version": "1.0.1",
        "timestamp": datetime.utcnow().isoformat(),
        "total_verifications": total,
        "message": "PAYKX Rail Verification API is running successfully",
        "mode": "shadow",
        "environment": "shadow-demo"
    }

# ─────────────────────────────────────────
# VERIFY ENDPOINT
# ─────────────────────────────────────────
@app.post("/api/v1/verify")
def verify(
    request: VerifyRequest,
    db: Session = Depends(get_db),
    api_key: str = Depends(require_api_key),
    mode: str = Query("live", enum=["live", "shadow"])
):
    corridor = request.corridor.upper()

    if is_in_cooldown(corridor) and mode == "live":
        return {"decision": "NO-GO", "reason": "Circuit breaker active", "status": "COOLDOWN"}

    # Mock probes
    behavioral_score = random.uniform(0.1, 0.9)
    behavioral_reason = "Velocity spike detected" if behavioral_score > 0.7 else "Clean"

    network_score = random.uniform(0.05, 0.5)
    network_reason = "High latency" if network_score > 0.4 else "Stable"

    historical_score = random.uniform(0.2, 0.8)
    historical_reason = "New pair flagged" if historical_score > 0.6 else "Established"

    score = (
        behavioral_score * settings.PROBE_WEIGHTS['behavioral'] +
        network_score * settings.PROBE_WEIGHTS['network'] +
        historical_score * settings.PROBE_WEIGHTS['historical']
    )

    probe_details = f"Behavioral: {behavioral_score:.2f} ({behavioral_reason}); Network: {network_score:.2f} ({network_reason}); Historical: {historical_score:.2f} ({historical_reason})"

    decision = "GO" if score >= settings.GO_THRESHOLD else "NO-GO"

    if decision == "NO-GO" and mode == "live":
        activate_cooldown(corridor)

    # Save to DB
    record = Verification(
        corridor=corridor,
        decision=decision,
        score=score,
        volatility=0.0,
        status="ACTIVE",
        mode=mode,
        probe_details=probe_details
    )
    db.add(record)
    db.commit()

    return {
        "decision": decision if mode == "live" else f"SHADOW: {decision}",
        "score": round(score, 2),
        "probe_details": probe_details,
        "demo_mode": True,
        "timestamp": datetime.utcnow().isoformat()
    }

# ─────────────────────────────────────────
# REQUEST TECHNICAL ACCESS
# ─────────────────────────────────────────
@app.post("/api/v1/request-access")
def request_access(request: AccessRequest, db: Session = Depends(get_db)):
    access_record = AccessRequest(
        name=request.name,
        email=request.email,
        reason=request.reason
    )
    db.add(access_record)
    db.commit()

    return {
        "message": "Access request received. We'll review and send an API key shortly.",
        "timestamp": datetime.utcnow().isoformat()
    }
