# 🎬 API de Filmes

Uma API REST para cadastro de filmes, desenvolvida com **FastAPI**, utilizando **SQLAlchemy** para persistência de dados em **SQLite**.

Este projeto faz parte de um desafio técnico com o objetivo de implementar um CRUD completo de filmes, expondo uma API REST funcional, organizada e de fácil manutenção.

---

## 🚀 Tecnologias utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [Docker](https://www.docker.com/)

📚 **Referência complementar**:  
[Guia sobre ORMs em Python – Real Python](https://realpython.com/python-sql-libraries/#object-relational-mappers-orms)

---

## 🗂️ Funcionalidades

- ✅ Criar um novo filme (`POST /filmes/`)
- ✅ Listar todos os filmes cadastrados (`GET /filmes/`)
- ✅ Buscar um filme por ID (`GET /filmes/{id}`)
- ✅ Atualizar um filme (`PUT /filmes/{id}`)
- ✅ Deletar um filme (`DELETE /filmes/{id}`)

---

## 📁 Estrutura de diretórios
movies-api/
├── app/
│ ├── api/ # Arquivos de rota (endpoints)
│ ├── crud/ # Funções de acesso ao banco
│ ├── db/ # Conexão e base do SQLAlchemy
│ ├── models/ # Modelos do banco (ORM)
│ ├── schemas/ # Schemas Pydantic
│ └── main.py # Ponto de entrada da aplicação
├── movies.db # Arquivo SQLite com os dados
├── .env # Variavel de conexão com o banco
├── dockerfile # Containerização
├── docker-compose.yml
└── README.md # Este arquivo
├── requirements.txt # Dependências do projeto    

---

## 🐳 Como rodar com Docker

1. Clone o repositório:

```bash
git clone https://github.com/gMoraes1/API-Filmes.git
cd API-Filmes
Construa e execute a aplicação com Docker Compose:
docker compose up 
A aplicação estará disponível em: http://localhost:8000/docs
⚠️ Atenção: O arquivo .env foi incluído neste repositório apenas por ser um desafio técnico.
Nunca suba esse tipo de arquivo em projetos reais, pois ele pode conter informações sensíveis, como senhas e logins.
