from fastapi import FastAPI, WebSocket
from typing import List

app = FastAPI()

# Store active WebSocket connections
clients: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()  # Keep connection open
    except:
        clients.remove(websocket)

# Function to send real-time updates
async def send_update(order_data):
    for client in clients:
        await client.send_json(order_data)
