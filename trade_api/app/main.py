from fastapi import FastAPI
from app.routes import router
from app.database import engine
from app.models import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Trade Order API", version="1.0")

# Include routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Trade Order API is running!"}
