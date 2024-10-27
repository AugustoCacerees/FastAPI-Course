from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: Optional[str] = None
    name: str
    purchase_price: float
    sales_price: float
    provider: str