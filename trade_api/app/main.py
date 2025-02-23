from fastapi import FastAPI, WebSocket
from app.routes import router  # Ensure routes are imported
from typing import List

app = FastAPI()

# Include API routes
app.include_router(router)

# Store active WebSocket clients
clients: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
    except:
        clients.remove(websocket)

# Function to broadcast updates
async def send_update(order_data):
    for client in clients:
        await client.send_json(order_data)
