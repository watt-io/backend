FROM python:3.8-slim-buster

WORKDIR /api

COPY api/requirements.txt api/requirements.txt

RUN pip install --no-cache-dir -r api/requirements.txt

COPY . .
