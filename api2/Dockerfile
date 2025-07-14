FROM python:3.10-slim

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    libglib2.0-0 libsm6 libxrender1 libxext6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir flask

CMD ["python", "app.py"]
