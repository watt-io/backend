# 🎬 FastAPI Filmes
API de gerenciamento de filmes desenvolvida em Python utilizando FastAPI, SQLAlchemy e SQLite.
O projeto foi estruturado seguindo boas práticas de orientação a objetos e inclui testes automatizados com pytest, além de suporte a Docker e docker-compose.

---

## 🚀 Tecnologias Utilizadas
- FastAPI – Framework para APIs rápidas

- SQLAlchemy – ORM para persistência de dados

- SQLite – Banco de dados leve

- Pydantic – Validação de dados

- Docker – Containerização

- Pytest – Testes automatizados

---

## 📂 Estrutura do Projeto
```bash
fastapi-filmes/
│── src/
│   ├── api/           # Rotas da aplicação
│   ├── core/          # Configurações
│   ├── db/            # Banco de dados
│   ├── schemas/       # Schemas Pydantic
│   ├── models/        # Tabelas do banco
│   ├── services/      # Regras de negócio
│   └── main.py        # Ponto de entrada da API
│
│── tests/             # Testes automatizados
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md
└── .gitignore
```

## ⚙️ Configuração do Ambiente
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/fastapi-filmes.git
cd fastapi-filmes
```

### 2️⃣ Criar ambiente virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

---

### ▶️ Executando a API Localmente
```bash
uvicorn src.main:app --reload
```
Acesse:

- Swagger: http://localhost:8000/docs

- ReDoc: http://localhost:8000/redoc

## 🐳 Executando com Docker
### 1️⃣ Build da imagem
```bash
docker-compose up --build
```

A API estará disponível em http://localhost:8000

## 🧪 Rodando Testes
Para rodar os testes unitários:

```bash
pytest tests/ --asyncio-mode=auto -v
```

##📌 Endpoints Disponíveis
- GET /filmes

Retorna a lista de filmes.

- POST /filmes

Cria um novo filme.

Exemplo:

```json
{
  "title": "Matrix",
  "director": "Wachowski",
  "year": 1999
}
```

- GET /filmes/{id}

Retorna um filme específico pelo ID.