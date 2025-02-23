from pydantic import BaseModel

class OrderCreate(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

class OrderResponse(OrderCreate):
    id: int

    class Config:
        orm_mode = True
