FROM python:3.9-slim

WORKDIR /backend

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "sql_apps.main:app", "--host=0.0.0.0", "--reload"]