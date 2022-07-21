FROM python
WORKDIR /app
COPY ./requirements.txt .
ADD ./app/cria_json.py /app/
ADD ./app/filmes_CRUD.py /app/
RUN pip install -r ./requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.app_api:app", "--host", "0.0.0.0", "--port", "80"]
