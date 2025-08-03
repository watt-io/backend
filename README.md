![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

## 👨‍💻 Desenvolvedor

**Bruno Ricardo Alves Pultz** - Desenvolvimento completo do CRUD de filmes com FastAPI

## 📋 Sobre o Projeto

Este é um fork do desafio WATT Filmes, implementando um CRUD completo com autenticação JWT, testes unitários e containerização Docker.

**Repositório**: [https://github.com/BrunoPultz/watt-backend](https://github.com/BrunoPultz/watt-backend)

#### Description

The challenge consists of implementing a movie CRUD using [python](https://www.python.org/ "python") integrating with a REST API and possible data persistence.

API Routes:

- `/movies` - [GET] should return all registered movies.
- `/movies` - [POST] should register a new movie.
- `/movies/{id}` - [GET] should return the movie with specified ID.

O Objetivo é te desafiar e reconhecer seu esforço para aprender e se adaptar. Qualquer código enviado, ficaremos muito felizes e avaliaremos com toda atenção!

#### Suggested Tools

It's not mandatory to use all suggested technologies, but it will be a differential =]

- Object-oriented programming (use objects, classes to manipulate movies)
- [FastAPI](https://fastapi.tiangolo.com/) (API with auto-generated documentation)
- [Docker](https://www.docker.com/) / [Docker-compose](https://docs.docker.com/compose/install/) (Application should be in a docker container, and start should be with the command `docker-compose up`
- Database integration (persist information in json (beginner) /[SqLite](https://www.sqlite.org/index.html) / [SQLAlchemy](https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases) / other DBs)

## 🚀 How to run the application

### Prerequisites

- Docker and Docker Compose installed
- Git

### Steps to run

1. **Clone the repository**

```bash
git clone <repository-url>
cd watt-backend
```

2. **Run with Docker Compose**

**Windows (PowerShell):**

**Option 1 - Automatic script:**

```powershell
powershell -ExecutionPolicy Bypass -File run.ps1
```

**Option 2 - Manual:**

```powershell
# Add Docker to current session PATH
$env:PATH += ";C:\Program Files\Docker\Docker\resources\bin"

# Run the application
docker compose up --build
```

**Option 3 - Full path:**

```powershell
& "C:\Program Files\Docker\Docker\resources\bin\docker.exe" compose up --build
```

**Linux/Mac:**

```bash
docker-compose up
```

3. **Access the API**

- **API**: http://localhost:8000
- **Swagger Documentation**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc

### 🎯 API Routes

#### Authentication

- `POST /auth/register` - Register new user
- `POST /auth/login` - Login (returns JWT token)
- `GET /auth/me` - View logged user data

#### Users (CRUD)

- `GET /users` - List all users (protected)
- `GET /users/{id}` - View specific user (protected)
- `PUT /users/{id}` - Update user (protected - own profile only)
- `DELETE /users/{id}` - Remove user (protected - own profile only)

#### Movies (CRUD)

- `GET /movies` - List all movies (public)
- `POST /movies` - Register new movie (protected)
- `GET /movies/{id}` - View specific movie (public)
- `PUT /movies/{id}` - Update movie (protected)
- `DELETE /movies/{id}` - Remove movie (protected)

### 🔐 Autenticação

Para acessar rotas protegidas, use o token JWT no header:

```
Authorization: Bearer <seu-token-jwt>
```

### 📝 Exemplo de uso

1. **Cadastrar usuário:**

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@exemplo.com", "password": "123456", "name": "João"}'
```

2. **Fazer login:**

```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@exemplo.com", "password": "123456"}'
```

3. **Cadastrar filme (com token):**

```bash
curl -X POST "http://localhost:8000/movies" \
  -H "Authorization: Bearer <seu-token>" \
  -H "Content-Type: application/json" \
  -d '{"title": "The Godfather", "year": 1972, "director": "Francis Ford Coppola", "genre": "Drama", "duration": 175, "rating": 9.2}'
```

4. **Listar todos os usuários (com token):**

```bash
curl -X GET "http://localhost:8000/users" \
  -H "Authorization: Bearer <seu-token>"
```

5. **Atualizar usuário (com token):**

```bash
curl -X PUT "http://localhost:8000/users/1" \
  -H "Authorization: Bearer <seu-token>" \
  -H "Content-Type: application/json" \
  -d '{"name": "João Silva", "email": "joao.silva@exemplo.com"}'
```

6. **Deletar usuário (com token):**

```bash
curl -X DELETE "http://localhost:8000/users/1" \
  -H "Authorization: Bearer <seu-token>"
```

### 🧪 Executando os Testes

Para executar os testes unitários:

```bash
# Executar todos os testes
pytest

# Executar com mais detalhes
pytest -v

# Executar testes específicos
pytest tests/test_auth.py

# Executar com cobertura (se instalado)
pytest --cov=app

# Executar apenas testes rápidos
pytest -m "not slow"
```

**Cobertura de Testes:**

- ✅ **Rotas de Autenticação** - Registro, login, verificação de usuário
- ✅ **Rotas de Filmes** - CRUD completo com autenticação
- ✅ **Rotas de Usuários** - CRUD completo com proteções de segurança
- ✅ **Operações CRUD** - Testes unitários para todas as operações
- ✅ **Autenticação JWT** - Criação, verificação e manipulação de tokens
- ✅ **Validação de Dados** - Schemas Pydantic e validações
- ✅ **Segurança** - Hash de senhas, proteções de acesso

### 🛠️ Tecnologias utilizadas

- **Python 3.11** - Linguagem principal
- **FastAPI** - Framework web com documentação automática
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados
- **Alembic** - Controle de versão do banco (migrações)
- **JWT** - Autenticação com tokens
- **Docker** - Containerização
- **Pydantic** - Validação de dados
- **Pytest** - Framework de testes unitários

### 📁 Estrutura do projeto

```
watt-backend/
├── app/
│   ├── main.py              # Aplicação FastAPI
│   ├── models/              # Modelos SQLAlchemy
│   ├── schemas/             # Schemas Pydantic
│   ├── crud/                # Operações CRUD
│   ├── database/            # Configuração do banco
│   ├── routes/              # Rotas da API
│   ├── auth/                # Autenticação JWT
│   └── middleware/          # Middleware de autenticação
├── tests/                   # Testes unitários
│   ├── conftest.py          # Configuração do pytest
│   ├── test_auth.py         # Testes de autenticação
│   ├── test_filmes.py       # Testes de filmes
│   ├── test_usuarios.py     # Testes de usuários
│   ├── test_crud.py         # Testes CRUD
│   └── test_auth_jwt.py     # Testes JWT
├── alembic/                 # Migrações do banco
│   ├── versions/            # Arquivos de migração
│   ├── env.py               # Configuração do Alembic
│   └── script.py.mako       # Template de migração
├── data/                    # Banco SQLite
├── Dockerfile              # Container da aplicação
├── docker-compose.yml      # Orquestração
├── alembic.ini             # Configuração do Alembic
├── pytest.ini             # Configuração do pytest
└── requirements.txt        # Dependências Python
```

#### Dúvidas?

Qualquer dúvida / sugestão / melhoria / orientação adicional só enviar email para hendrix@wattio.com.br

Salve!
