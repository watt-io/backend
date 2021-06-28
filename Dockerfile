FROM python:3.8
WORKDIR /code

RUN pip install fastapi uvicorn
RUN pip install redis

EXPOSE 8000
COPY . .
CMD ["python", "main.py"]