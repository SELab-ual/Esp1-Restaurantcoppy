from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from .db import SessionLocal, init_db
from .models import MenuItem, Order
from .schemas import MenuItemOut, OrderCreate, OrderOut
from .audit import record
from .sample_data import seed
import os

app = FastAPI(title="RMOS Sprint1 Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()
    seed()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/keepalive")
def keepalive():
    return {"status": "alive"}

@app.get("/menu", response_model=list[MenuItemOut])
def get_menu():
    db = SessionLocal()
    try:
        items = db.query(MenuItem).all()
        return items
    finally:
        db.close()

@app.post("/orders", response_model=OrderOut)
def create_order(order: OrderCreate, request: Request):
    db = SessionLocal()
    try:
        o = Order(table_number=order.table_number, items=order.items, status="pending")
        db.add(o)
        db.commit()
        db.refresh(o)
        record("order_created", {"order_id": o.id, "items": order.items, "table": order.table_number})
        return o
    finally:
        db.close()

@app.post("/orders/{order_id}/accept", response_model=OrderOut)
def accept_order(order_id: int):
    db = SessionLocal()
    try:
        o = db.query(Order).filter(Order.id == order_id).first()
        if not o:
            raise HTTPException(status_code=404, detail="Order not found")
        o.status = "accepted"
        db.add(o)
        db.commit()
        db.refresh(o)
        record("order_accepted", {"order_id": o.id})
        return o
    finally:
        db.close()

@app.get("/orders/pending", response_model=list[OrderOut])
def pending_orders():
    db = SessionLocal()
    try:
        return db.query(Order).filter(Order.status == "pending").all()
    finally:
        db.close()