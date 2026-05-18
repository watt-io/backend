# API REST CRUD de Filmes

API REST para cadastro e consulta de filmes, desenvolvida como solução do desafio técnico Wattio. A aplicação sobe inteiramente via Docker — não é necessário instalar Python ou dependências na máquina host.

As rotas de filmes são protegidas por **autenticação JWT (Bearer)**. Um usuário padrão é configurado no arquivo `.env` para obter o token de acesso.

## Tecnologias utilizadas

- **Python 3.12+**
- **FastAPI** — framework web assíncrono
- **Pydantic v2** — validação de schemas
- **JWT (python-jose)** — tokens de autenticação Bearer
- **SQLAlchemy (async)** — ORM com driver `asyncpg`
- **Alembic** — migrations do banco de dados
- **PostgreSQL 16** — persistência
- **Nginx** — reverse proxy (porta 80)
- **Docker + Docker Compose** — orquestração dos serviços

## Pré-requisitos

- [Docker](https://www.docker.com/) e Docker Compose

## Como executar

```bash
git clone <url-do-repositorio>
cd backend
cp .env.example .env
docker compose up --build
```

API em **[http://localhost](http://localhost)** (porta 80). Para parar: `docker compose down`.

## Variáveis de ambiente

```env
POSTGRES_USER=filmes_user
POSTGRES_PASSWORD=filmes_secret
POSTGRES_DB=filmes_db
DATABASE_URL=postgresql+asyncpg://filmes_user:filmes_secret@db:5432/filmes_db

AUTH_USERNAME=admin
AUTH_PASSWORD=admin123

JWT_SECRET_KEY=change-me-in-production-use-long-random-string
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
```

## Autenticação

1. **Login:** `POST /auth/token` com `username` e `password` (form-urlencoded), usando os valores de `AUTH_USERNAME` e `AUTH_PASSWORD` do `.env`.
2. **Demais rotas:** header `Authorization: Bearer <access_token>`.

Documentação interativa:

- **Swagger UI:** [http://localhost/docs](http://localhost/docs) — testar rotas (botão **Authorize** com usuário/senha do `.env`)
- **ReDoc:** [http://localhost/redoc](http://localhost/redoc) — leitura da API (sem executar requisições)

## Rotas


| Método | Rota           | Auth   | Descrição     |
| ------ | -------------- | ------ | ------------- |
| POST   | `/auth/token`  | Não    | Login → JWT   |
| GET    | `/filmes`      | Bearer | Lista filmes  |
| POST   | `/filmes`      | Bearer | Cria filme    |
| GET    | `/filmes/{id}` | Bearer | Busca por ID  |
| DELETE | `/filmes/{id}` | Bearer | Remove por ID |


## Respostas por endpoint

### `POST /auth/token`

**Request** — `Content-Type: application/x-www-form-urlencoded`


| Campo      | Tipo   | Obrigatório |
| ---------- | ------ | ----------- |
| `username` | string | Sim         |
| `password` | string | Sim         |


**200 OK**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

### `GET /filmes`

**200 OK** — lista de filmes (vazia se não houver registros)

```json
[
  {
    "id": 1,
    "titulo": "O Poderoso Chefão",
    "diretor": "Francis Ford Coppola",
    "ano": 1972,
    "genero": "Drama",
    "sinopse": "A saga da família Corleone no submundo do crime organizado."
  }
]
```

```json
[]
```

---

### `POST /filmes`

**Request** — `Content-Type: application/json`

```json
{
  "titulo": "Matrix",
  "diretor": "Lana e Lilly Wachowski",
  "ano": 1999,
  "genero": "Ficção científica",
  "sinopse": "Um hacker descobre que a realidade é uma simulação controlada por máquinas."
}
```


| Campo     | Tipo   | Regras             |
| --------- | ------ | ------------------ |
| `titulo`  | string | 1–255 caracteres   |
| `diretor` | string | 1–255 caracteres   |
| `ano`     | int    | entre 1888 e 2100  |
| `genero`  | string | 1–100 caracteres   |
| `sinopse` | string | mínimo 1 caractere |


**201 Created**

```json
{
  "id": 1,
  "titulo": "Matrix",
  "diretor": "Lana e Lilly Wachowski",
  "ano": 1999,
  "genero": "Ficção científica",
  "sinopse": "Um hacker descobre que a realidade é uma simulação controlada por máquinas."
}
```

---

### `GET /filmes/{id}`

**200 OK**

```json
{
  "id": 1,
  "titulo": "Matrix",
  "diretor": "Lana e Lilly Wachowski",
  "ano": 1999,
  "genero": "Ficção científica",
  "sinopse": "Um hacker descobre que a realidade é uma simulação controlada por máquinas."
}
```

**404 Not Found**

```json
{
  "detail": "Filme não encontrado"
}
```

---

### `DELETE /filmes/{id}`

**204 No Content** — corpo vazio.

**404 Not Found**

```json
{
  "detail": "Filme não encontrado"
}
```

## Erros da API


| Código  | Rota / contexto       | Quando ocorre                           | `detail`                                  |
| ------- | --------------------- | --------------------------------------- | ----------------------------------------- |
| **401** | `POST /auth/token`    | Usuário ou senha diferentes do `.env`   | `"Usuário ou senha incorretos"`           |
| **401** | `/filmes` (todas)     | Sem header `Authorization`              | `"Not authenticated"`                     |
| **401** | `/filmes` (todas)     | Token inválido, malformado ou expirado  | `"Credenciais inválidas"`                 |
| **404** | `GET /filmes/{id}`    | ID não existe                           | `"Filme não encontrado"`                  |
| **404** | `DELETE /filmes/{id}` | ID não existe                           | `"Filme não encontrado"`                  |
| **404** | Qualquer              | URL não registrada na API               | `"Not Found"`                             |
| **422** | `POST /auth/token`    | Formulário sem `username` ou `password` | Lista de erros Pydantic (`loc`, `msg`, …) |
| **422** | `POST /filmes`        | JSON inválido ou campos fora das regras | Lista de erros Pydantic (`loc`, `msg`, …) |


Demais erros (401, 422, rota inexistente): veja tabela abaixo.

## Exemplos (curl)

```bash
# Login
TOKEN=$(curl -s -X POST http://localhost/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123" \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

# Listar
curl -H "Authorization: Bearer $TOKEN" http://localhost/filmes

# Criar
curl -X POST http://localhost/filmes \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Interestelar",
    "diretor": "Christopher Nolan",
    "ano": 2014,
    "genero": "Ficção científica",
    "sinopse": "Exploradores viajam por um buraco de minhoca em busca de um novo lar para a humanidade."
  }'

# Buscar por ID
curl -H "Authorization: Bearer $TOKEN" http://localhost/filmes/1

# Excluir
curl -X DELETE -H "Authorization: Bearer $TOKEN" http://localhost/filmes/1
```

Ajuste `username`/`password` no login se alterou o `.env`.

## Estrutura do projeto

```
backend/
├── app/
│   ├── main.py              # Aplicação FastAPI e lifespan
│   ├── config.py            # Configurações (variáveis de ambiente)
│   ├── database.py          # Engine e sessão async
│   ├── auth/                # JWT e dependências de autenticação
│   ├── models/              # Modelos SQLAlchemy
│   ├── schemas/             # Schemas Pydantic v2 (filmes, auth)
│   ├── repositories/        # Camada de acesso a dados
│   └── routers/             # Rotas HTTP (auth, filmes)
├── migrations/              # Migrations Alembic
├── nginx/
│   └── nginx.conf           # Configuração do reverse proxy
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── docker-entrypoint.sh
├── requirements.txt
├── .env.example
└── README.md
```

## Arquitetura

```
Cliente → Nginx (:80) → FastAPI/Uvicorn (:8000) → PostgreSQL
                              ↑
                         Alembic (migrations no startup)
```

Migrations rodam no startup do container (`alembic upgrade head`)

