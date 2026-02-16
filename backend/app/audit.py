from .db import SessionLocal
from .models import Audit
import json

def record(event: str, payload: dict | None = None):
    db = SessionLocal()
    try:
        a = Audit(event=event, payload=payload or {})
        db.add(a)
        db.commit()
    finally:
        db.close()