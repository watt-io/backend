# API de Filmes - WATTIO

Este projeto consiste na implementação de uma API REST de filmes utilizando Python com FastAPI.

## Funcionalidades

- Listar todos os filmes
- Cadastrar um novo filme
- Buscar filme por ID
- Atualizar filme
- Remover filme

## Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Docker
- Docker Compose

## Como executar o projeto

### Usando Docker

```bash
docker compose up --build
```

A aplicação estará disponível em:
```bash
http://127.0.0.1:8000/docs
```

## Exemplos de uso da API

### Criar um filme
POST /filmes
```bash
{
  "titulo": "Interestelar",
  "diretor": "Christopher Nolan",
  "ano": 2014,
  "genero": "Ficção científica"
}

```

Resposta esperada

```bash
{  
  "titulo": "Interestelar",
  "diretor": "Christopher Nolan",
  "ano": 2014,
  "genero": "Ficção científica",
  "id": 1
}

```
