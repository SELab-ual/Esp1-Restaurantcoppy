from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, JSON, func
from sqlalchemy.orm import relationship
from .db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)  # 'waiter' or 'supervisor'

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price_cents = Column(Integer, nullable=False)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    table_number = Column(String, nullable=True)
    status = Column(String, default="pending")  # pending, accepted, preparing, served
    items = Column(JSON, nullable=False)  # list of {item_id, qty}
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Audit(Base):
    __tablename__ = "audit"
    id = Column(Integer, primary_key=True)
    event = Column(String, nullable=False)
    payload = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())