
# Desafio CRUD de Filmes - Backend Python

Este projeto implementa um CRUD de filmes utilizando FastAPI, SQLAlchemy e PostgreSQL, com suporte a Docker e pgAdmin para gerenciamento do banco de dados.

## Como rodar o projeto

### Pré-requisitos
- Docker e Docker Compose instalados

### Passos
1. Clone o repositório e acesse a pasta `backend`.
2. Crie um arquivo chamado `.env` na raiz da pasta `backend` com o seguinte conteúdo:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=pedro12
POSTGRES_DB=filmes
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

3. Execute o comando abaixo para subir todos os serviços (API, banco de dados e pgAdmin):

```
docker-compose up --build
```

4. Acesse a documentação da API em: [http://localhost:8000/docs](http://localhost:8000/docs)
	- Aqui você pode testar as rotas `/filmes` (GET, POST) e `/filmes/{id}` (GET).

5. Acesse o pgAdmin em: [http://localhost:5050](http://localhost:5050)
	- Login: `admin@admin.com`
	- Senha: `pedro12`
	- Para conectar ao banco, use:
	  - Host: `db`
	  - Usuário: `postgres`
	  - Senha: `pedro12`
	  - Database: `filmes`

6. Para parar todos os serviços, use:

```
docker-compose down
```

## Estrutura dos arquivos principais
- `main.py`: API FastAPI com as rotas do CRUD
- `models.py`: Modelos ORM e schemas Pydantic
- `database.py`: Configuração da conexão com PostgreSQL
- `docker-compose.yml`: Orquestração dos serviços
- `Dockerfile`: Build do backend
- `.env`: Variáveis de ambiente do banco

## Observações
- O banco de dados é criado automaticamente ao subir os containers.
- As tabelas são criadas automaticamente pelo SQLAlchemy.
