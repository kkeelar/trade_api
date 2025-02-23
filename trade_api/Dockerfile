# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies, including WebSockets
RUN pip install --no-cache-dir uvicorn[standard] fastapi sqlalchemy psycopg2-binary websockets

# Expose port 8000
EXPOSE 8000

# Run FastAPI with WebSocket support
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
