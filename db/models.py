from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base

class Verification(Base):
    __tablename__ = "verifications"

    id = Column(Integer, primary_key=True, index=True)
    corridor = Column(String, index=True)
    decision = Column(String)
    score = Column(Float)
    volatility = Column(Float)
    status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    mode = Column(String, default="live")
    probe_details = Column(String)

class AccessRequest(Base):
    __tablename__ = "access_requests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    reason = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="PENDING")
