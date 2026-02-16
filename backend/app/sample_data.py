from .db import SessionLocal, init_db
from .models import MenuItem, User
from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def seed():
    init_db()
    db = SessionLocal()
    try:
        if db.query(MenuItem).count() == 0:
            items = [
                MenuItem(name="Margherita Pizza", description="Tomato, mozzarella", price_cents=900),
                MenuItem(name="Caesar Salad", description="Romaine, parmesan", price_cents=700),
                MenuItem(name="Espresso", description="Strong coffee", price_cents=200),
            ]
            db.add_all(items)
        if db.query(User).count() == 0:
            waiter = User(username="waiter1", password_hash=pwd_ctx.hash("waiterpass"), role="waiter")
            db.add(waiter)
        db.commit()
    finally:
        db.close()