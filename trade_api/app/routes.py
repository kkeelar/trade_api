from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud
from app.main import send_update  # Import WebSocket update function

router = APIRouter()

@router.post("/orders", response_model=schemas.OrderResponse)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    new_order = crud.create_order(db, order)
    await send_update(new_order.dict())  # Send real-time update
    return new_order

@router.get("/orders", response_model=list[schemas.OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)
