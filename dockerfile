# syntax=docker/dockerfile:1

FROM python:3.10.4-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN python models.py

RUN python create.py

CMD [ "python", "-m" , "uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "8000"]