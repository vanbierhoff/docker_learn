FROM python:3.12-bookworm

WORKDIR /app

COPY . /app

RUN pip install -r ./requirements.txt && pip install psycopg2-binary



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]