# Watt-io Movies API

API REST para CRUD de filmes, feita em Python com FastAPI e SQLite.

## Stack

- Python (Docker usa 3.11)
- FastAPI + Pydantic
- SQLite
- Docker / Docker Compose

## Rotas da API

- `POST /movies`
- `GET /movies`
- `GET /movies/{id}`

## Estrutura do projeto

```
src/
  main/
    database/
    repositories/
    routes/
    server/
    services/
    validators/
run.py
```

## Como rodar (local)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

A API sobe em `http://localhost:3009`.

## Como rodar (Docker)

```bash
docker-compose up --build
```

Para parar:

```bash
docker-compose down
```

## Swagger / OpenAPI

- http://localhost:3009/docs
- http://localhost:3009/openapi.json

## Banco de dados

- SQLite cria o arquivo `wattio.db` na raiz do projeto na primeira execucao.
- No Docker, o banco fica dentro do container (nao persiste entre recriacoes).
