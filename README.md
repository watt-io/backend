# 🎬 API de Filmes

API REST para gerenciamento de filmes, desenvolvida com FastAPI, utilizando SQLite para persistência de dados e Docker para containerização.

---

## 🚀 Tecnologias utilizadas

* Python 3.11
* FastAPI
* SQLAlchemy
* SQLite
* Docker / Docker Compose

---

## 📁 Estrutura do projeto

```
filmes-api/
│
├── app/
│   ├── main.py        # Rotas da API
│   ├── models.py      # Modelos do banco
│   ├── schemas.py     # Validação de dados
│   ├── crud.py        # Regras de negócio
│   └── database.py    # Conexão com banco
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Como executar o projeto

### 🔹 Usando Docker (recomendado)

```bash
docker-compose up --build
```

A aplicação estará disponível em:

```
http://localhost:8000
```

---

### 🔹 Executando localmente (sem Docker)

```bash
# criar ambiente virtual
python -m venv venv

# ativar ambiente
venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# rodar aplicação
uvicorn app.main:app --reload
```

---

## 📌 Endpoints

### 🔹 Listar todos os filmes

```
GET /filmes
```

---

### 🔹 Criar um novo filme

```
POST /filmes
```

Exemplo de body:

```json
{
  "titulo": "Batman",
  "descricao": "Filme do Cavaleiro das Trevas"
}
```

---

### 🔹 Buscar filme por ID

```
GET /filmes/{id}
```

---

## 📄 Documentação da API

A documentação interativa (Swagger) está disponível em:

```
http://localhost:8000/docs
```

---

## 💾 Persistência de dados

Os dados são armazenados em um banco SQLite local:

```
filmes.db
```

---

## 🐳 Containerização

A aplicação foi containerizada utilizando Docker, garantindo portabilidade e facilidade de execução em qualquer ambiente.

---

## ✨ Melhorias futuras

* Implementar PUT e DELETE (CRUD completo)
* Adicionar validações mais robustas
* Implementar testes automatizados
* Utilizar banco de dados relacional como PostgreSQL

---

## 👨‍💻 Autor

Gabriel Augusto
