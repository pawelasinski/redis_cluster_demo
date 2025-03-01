FROM python:3.9-slim

WORKDIR /app

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install --no-cache-dir -r requirements.txt

COPY tests/test_redis_cluster.py test_redis_cluster.py

RUN mkdir pytest_results
