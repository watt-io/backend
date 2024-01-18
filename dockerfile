FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install fastapi[all] uvicorn[standard] sqlalchemy databases psycopg2

WORKDIR /app

COPY ./app /app

EXPOSE 3000

CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:3000"]

