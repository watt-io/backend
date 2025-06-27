![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

# 🎬 Wattio Movie API

## 📄 Descrição

Este projeto é parte de um desafio técnico da empresa **Wattio**, que consiste na implementação de uma **API RESTful para cadastro de filmes**. Foi desenvolvido com foco em boas práticas de engenharia de software, utilizando **arquitetura hexagonal (Ports and Adapters)**, com **Python (FastAPI)**, **Docker**, e **PostgreSQL** para persistência de dados.

---

## 🧱 Arquitetura Hexagonal

A aplicação foi estruturada seguindo o padrão de **Arquitetura Hexagonal**, separando claramente:

- **Domínio (Regras de negócio)** — `src/core`
- **Ports (Interfaces)** — `src/core/ports`
- **Adapters (Implementações)** — `src/adapters/driven` e `src/adapters/driving`
- **Entrypoint da aplicação** — `app.py` (FastAPI)

Esse modelo promove uma aplicação mais desacoplada, testável e preparada para evoluções futuras.

---

## 🚀 Tecnologias Utilizadas

- 🐍 Python
- ⚡ FastAPI
- 🐘 PostgreSQL
- 🐳 Docker & Docker Compose
- 📦 Poetry (gerenciador de dependências)
- 🔁 SQLAlchemy (ORM)

---

## 📌 Rotas da API

| Método | Rota              | Descrição                                 |
|--------|-------------------|-------------------------------------------|
| GET    | `/filmes`         | Retorna todos os filmes cadastrados       |
| POST   | `/filmes`         | Cadastra um novo filme                    |
| GET    | `/filmes/{id}`    | Retorna um filme específico pelo ID       |
| PUT    | `/filmes/{id}`    | Atualiza um filme pelo ID                 |
| DELETE | `/filmes/{title}` | Deleta um filme pelo título               |

A documentação interativa da API pode ser acessada em:

http://localhost:8000/docs


## ▶️ Como rodar a aplicação

### 1. Clone o repositório
```bash
git clone https://github.com/limagustavo2200/caseWattio.git
cd caseWatiio

2. Suba os containers com Docker Compose

docker-compose up --build

Isso irá:

Instanciar o serviço da API com FastAPI

Criar um banco de dados PostgreSQL via Docker

3. Criar as tabelas no banco de dados

Com os containers em execução, execute o script de criação de tabelas:

docker-compose exec app poetry run python src/adapters/driven/database/create_tables.py

Esse script cria as tabelas definidas no ORM, conectando-se ao banco PostgreSQL.
```


## 🧪 Testando a API

Com a aplicação rodando, você pode acessar:

📘 Documentação Swagger:
http://localhost:8000/docs

📗 Redoc (documentação alternativa):
http://localhost:8000/redoc


## 📫 Contato

Dúvidas ou sugestões? Entre em contato pelo [LinkedIn](https://www.linkedin.com/in/seu-usuario/).

---