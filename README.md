![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

# API de Filmes - Desafio Wattio

API REST para gerenciamento de filmes, desenvolvida com FastAPI, SQLAlchemy e SQLite.

## Tecnologias

- Python 3.13
- FastAPI
- SQLAlchemy 2.0
- SQLite
- Pydantic V2
- Pytest
- Docker / Docker Compose

## Como Rodar

### Com Docker (recomendado)

```bash
docker compose up --build
```

A API estará disponível em: http://localhost:8000

### Sem Docker

```bash
# Criar e ativar o ambiente virtual (Windows)
python -m venv .venv
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor
uvicorn app.main:app --reload
```

## Documentação da API

Com o servidor rodando, acesse a documentação interativa:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

| Método   | Rota            | Descrição                          |
|----------|-----------------|------------------------------------|
| GET      | /filmes         | Listar filmes (com filtros e paginação) |
| POST     | /filmes         | Cadastrar novo filme               |
| GET      | /filmes/{id}    | Buscar filme por ID                |
| PUT      | /filmes/{id}    | Atualizar filme                    |
| DELETE   | /filmes/{id}    | Remover filme                      |

### Filtros e Paginação

```
GET /filmes?genero=Drama&diretor=Coppola&ano=1972&skip=0&limit=10
```

| Parâmetro | Tipo   | Descrição                          |
|-----------|--------|------------------------------------|
| genero    | string | Filtra por gênero (case-insensitive) |
| diretor   | string | Filtra por diretor (case-insensitive) |
| ano       | int    | Filtra por ano de lançamento       |
| skip      | int    | Registros a pular (padrão: 0)      |
| limit     | int    | Máximo de resultados (padrão: 10)  |

### Exemplo de Requisição - Criar Filme

```bash
curl -X POST http://localhost:8000/filmes \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "O Poderoso Chefão",
    "diretor": "Francis Ford Coppola",
    "ano": 1972,
    "genero": "Drama"
  }'
```

**Resposta (201):**
```json
{
  "titulo": "O Poderoso Chefão",
  "diretor": "Francis Ford Coppola",
  "ano": 1972,
  "genero": "Drama",
  "id": 1
}
```

## Testes

### Localmente

```bash
pytest tests/ -v
```

### Com Docker

```bash
docker compose run --rm tests
```

**Testes incluídos:**
- Criação de filmes (campos válidos e inválidos)
- Listagem com filtros e paginação
- Busca por ID (existente e inexistente)
- Atualização parcial de campos
- Remoção de filmes
- Validação de dados (422)
- Tratamento de erros (400, 404)

## Estrutura do Projeto

```
backend/
├── app/
│   ├── database.py     # Configuração do banco de dados (SQLAlchemy)
│   ├── main.py         # Ponto de entrada e rotas (FastAPI)
│   ├── models.py       # Definição das tabelas no banco de dados
│   └── schemas.py      # Validação de dados de entrada/saída (Pydantic)
├── tests/
│   └── test_filmes.py  # Testes de integração (Pytest)
├── Dockerfile          # Configuração da imagem Docker
├── docker-compose.yml  # Orquestração dos serviços (API e testes)
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação principal
```

