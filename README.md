# Wattio Backend Challenge

![WATTIO](https://www.wattio.com.br/identidade-wattio/logo-marca-horizontal-azul.svg)

CRUD de Filmes com Python, FastAPI e Docker.

Este repositório contém um desafio técnico que consiste na implementação de um CRUD de filmes utilizando Python, FastAPI, e integração com uma API REST, além de persistência de dados em PostgreSQL. O projeto é containerizado com Docker para facilitar a execução e o deploy.

## Tecnologias Utilizadas
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [uv](https://docs.astral.sh/uv/)
- [Python](https://www.python.org/)
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
  - [Alembic](https://alembic.sqlalchemy.org/en/latest/)
  - [psycopg](https://www.psycopg.org/)

## Pré-requisitos
- [Docker](https://www.docker.com/) instalado (opcional mas recomendado)
- [Python 3.12+](https://www.python.org/) instalado (para execução manual)
- [uv](https://docs.astral.sh/uv/) instalado (opcional para gestão de ambiente virtual)

## Como executar
Clone o repositório
   ```bash
   git clone https://github.com/araujogusta/watt-io-backend-challenge.git
   cd watt-io-backend-challenge
   ```

### Utilizando Docker (Recomendado)
Execute o comando `docker compose up` para iniciar o container.

### Manualmente
1. Crie um ambiente virtual e ative-o.
    ```bash
    python -m venv .venv # ou
    uv venv 

    .venv\Scripts\activate # no Windows
    source .venv/bin/activate # no Linux ou MacOS
    ```
2. Instale as dependências utilizando o comando `pip install .`.
3. Crie um arquivo `.env` na raiz do projeto e insira suas credenciais do banco de dados. Utilize o arquivo `.env.example` como exemplo.
4. Execute as migrações utilizando o comando `alembic upgrade head`.
5. Inicie o servidor usando o comando `fastapi dev movies/run.py`.

## Como utilizar

O servidor estará disponível em `http://localhost:8000`.

Você pode acessar a documentação interativa da API:
- [Swagger UI](http://localhost:8000/docs)
- [ReDoc](http://localhost:8000/redoc)

---

### Rotas da API

#### `GET /filmes`
Retorna todos os filmes cadastrados no banco de dados.

**Exemplo de requisição**
```http
GET http://localhost:8000/filmes
````

**Resposta esperada**

```json
[
  {
    "id": 1,
    "title": "Inception",
    "overview": "A mind-bending thriller about dream invasion.",
    "year": 2010,
    "rating": 8.8,
    "category": "Sci-Fi"
  },
  {
    "id": 2,
    "title": "The Matrix",
    "overview": "A computer hacker learns about the true nature of reality.",
    "year": 1999,
    "rating": 8.7,
    "category": "Action"
  }
]
```

---

#### `POST /filmes`

Cadastra um novo filme no banco de dados.

**Exemplo de requisição**

```http
POST http://localhost:8000/filmes
Content-Type: application/json

{
  "title": "Interstellar",
  "overview": "A team travels through a wormhole in search of a new home for humanity.",
  "year": 2014,
  "rating": 8.6,
  "category": "Sci-Fi"
}
```

**Resposta esperada**

```json
{
  "id": 3,
  "title": "Interstellar",
  "overview": "A team travels through a wormhole in search of a new home for humanity.",
  "year": 2014,
  "rating": 8.6,
  "category": "Sci-Fi"
}
```

---

#### `GET /filmes/{id}`

Retorna o filme com o ID especificado.

**Exemplo de requisição**

```http
GET http://localhost:8000/filmes/1
```

**Resposta esperada**

```json
{
  "id": 1,
  "title": "Inception",
  "overview": "A mind-bending thriller about dream invasion.",
  "year": 2010,
  "rating": 8.8,
  "category": "Sci-Fi"
}
```

**Resposta caso o filme não seja encontrado**

```json
{
  "detail": "Movie not found"
}
```

(status code: 404)

## Testes
Para executar os testes, utilize o comando:
```bash
pytest
# ou 
task test
```
## Autor
Gustavo Araujo - gusta01.oliveira@gmail.com