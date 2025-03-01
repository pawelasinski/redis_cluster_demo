FROM python:3.9-slim

WORKDIR /app

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install --no-cache-dir -r requirements.txt

COPY src/redis_cluster_app.py redis_cluster_app.py

RUN mkdir -p /app/logs

CMD ["python", "redis_cluster_app.py"]
