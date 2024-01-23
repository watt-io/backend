FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./app /app

# Instalação das dependências
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip==23.2.1
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt