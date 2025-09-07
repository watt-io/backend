## 🚀 Como subir a aplicação

### Pré-requisitos
- Python 3.12+
- SQLite

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd py-crud
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
Execute as migrações do Alembic para criar as tabelas:
```bash
alembic upgrade head
```

### 5. Execute a aplicação
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Acesse a aplicação
- **API**: http://localhost:8000
- **Documentação interativa (Swagger)**: http://localhost:8000/docs
- **Redoc**: http://localhost:8000/redoc

## 📋 Endpoints da API

### Filmes
- **GET** `/filmes/` - Lista todos os filmes
- **POST** `/filmes/` - Cria um novo filme
- **GET** `/filmes/{id}` - Busca filme por ID

### Exemplo de uso

#### Criar um filme
```bash
curl -X POST "http://localhost:8000/filmes/" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Inception",
    "ano": 2010,
    "duracao": 148,
    "diretor": "Christopher Nolan"
  }'
```

#### Listar filmes
```bash
curl -X GET "http://localhost:8000/filmes/"
```

## 🛠️ Tecnologias utilizadas

- **FastAPI**: Framework web para construção de APIs
- **SQLAlchemy**: ORM para Python
- **Alembic**: Ferramenta de migração de banco de dados
- **SQLite**: Banco de dados leve
- **Pydantic**: Validação de dados
- **Uvicorn**: Servidor ASGI

## 📁 Estrutura do projeto

```
py-crud/
├── app/
│   ├── api/
│   │   └── filme_routes.py      # Rotas da API
│   ├── core/
│   │   └── config.py            # Configurações
│   ├── crud/
│   │   └── filme_crud.py        # Operações CRUD
│   ├── db/
│   │   ├── base.py              # Base do SQLAlchemy
│   │   └── session.py           # Configuração da sessão
│   ├── models/
│   │   └── filme.py             # Modelo do banco
│   ├── schemas/
│   │   └── filme_schema.py      # Schemas Pydantic
│   └── main.py                  # Aplicação principal
├── alembic/                     # Migrações do banco
├── banco.db                     # Arquivo do banco SQLite
├── alembic.ini                  # Configuração do Alembic
└── requirements.txt             # Dependências
```

## 📝 Modelo de dados

### Filme
```json
{
  "id": 1,
  "titulo": "Inception",
  "ano": 2010,
  "duracao": 148,
  "diretor": "Christopher Nolan"
}
```
