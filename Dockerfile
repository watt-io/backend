FROM python:3.9-slim

WORKDIR /usr/app

RUN python -m pip install --upgrade pip

COPY ./ ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
