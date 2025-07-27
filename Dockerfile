FROM --platform=linux/amd64 python:3.10-slim

RUN apt-get update && apt-get install -y poppler-utils build-essential && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY main.py .

ENTRYPOINT ["python", "main.py"]
