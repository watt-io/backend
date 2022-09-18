FROM python:3.8-slim-buster


COPY .. /app
COPY requeriments.txt ../app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requeriments.txt

COPY . .

CMD ["uvicorn", "__init__:api", "--reload", "--host=0.0.0.0", "--port=3000"] 

#