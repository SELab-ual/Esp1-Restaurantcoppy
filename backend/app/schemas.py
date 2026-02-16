from pydantic import BaseModel
from typing import List, Optional

class MenuItemOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price_cents: int

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    table_number: Optional[str]
    items: List[dict]  # { "item_id": int, "qty": int }

class OrderOut(BaseModel):
    id: int
    table_number: Optional[str]
    status: str
    items: List[dict]

    class Config:
        orm_mode = True