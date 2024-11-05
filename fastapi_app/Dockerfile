# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend /app
COPY ./frontend /frontend
COPY ./database /database

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
