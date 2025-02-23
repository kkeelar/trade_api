from fastapi import FastAPI, WebSocket, APIRouter
from typing import List

app = FastAPI()
router = APIRouter()

# Store active WebSocket connections
clients: List[WebSocket] = []

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep connection open
    except:
        clients.remove(websocket)

# WebSocket Broadcast Function
async def send_update(order_data):
    for client in clients:
        await client.send_json(order_data)

app.include_router(router)  # Include routes in FastAPI
