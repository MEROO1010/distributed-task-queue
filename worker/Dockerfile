FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install celery redis

CMD ["celery", "-A", "celery_worker.celery_app", "worker", "--loglevel=info"]
