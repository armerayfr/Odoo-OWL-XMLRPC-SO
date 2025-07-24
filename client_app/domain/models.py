from pydantic import BaseModel
from typing import List

class SaleOrderLine(BaseModel):
    product_id: int
    quantity: float

class SaleOrderCreate(BaseModel):
    partner_id: int
    order_lines: List[SaleOrderLine]

class SaleOrderUpdate(BaseModel):
    sale_order_id: int
    updates: dict

class SaleOrderId(BaseModel):
    id: int
