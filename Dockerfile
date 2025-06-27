FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry


WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root --only main

COPY src/ ./src/

ENV PYTHONPATH=/app/src

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
