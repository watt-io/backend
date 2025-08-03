# Filmes API

API REST para cadastro e consulta de filmes, desenvolvida com FastAPI e SQLAlchemy, para desafio proposto por Watt-io.



## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Banco de dados SQLite (padrão)
- (Opcional) Docker e Docker Compose



## Instalação

1. **Clone o repositório**
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd filmes_api
   ```

2. **Crie e ative um ambiente virtual**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
   ```

4. **Sobre o banco de dados**
   - Por padrão, a API usa SQLite. Se quiser usar outro banco, ajuste a string de conexão no arquivo de configuração.



## Execução

Rode a aplicação com Docker, usando o comando dentro da pasta raíz do projeto:
```sh
docker run -d -p 8000:8000 filmes_api
```

ou

Execute pelo servidor de desenvolvimento, usando o comando dentro da pasta raíz do projeto:
```sh
uvicorn app.main:app --reload
```

Acesse a documentação auto-gerada com swagger em: [http://localhost:8000/docs]



## Estrutura do Projeto

```
filmes_api/
├── app/
│   ├── api/
|     ├── v1/
|        ├── routes_movies.py
│   ├── core/
|     ├── config.py
│   ├── crud/
|     ├── movie.py
│   ├── data/
│   ├── db/
|     ├── base.py
|     ├── init_db.py
|     ├── session.py
│   ├── models/
|     ├── movie.py
│   ├── schemas/
|     ├── movie.py
│   ├── __init__.py
│   └── main.py
├── data/
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```



## Endpoints Principais

- `GET /api/v1/routes_movies` — Lista todos os filmes
- `GET /api/v1/routes_movies/{id}` — Consulta filme por ID
- `GET /api/v1/routes_movies/title/{title}` — Lista filmes cujo o titulo contem string passada em {title}
- `POST /api/v1/routes_movies` — Cria um novo filme
- `PUT /api/v1/routes_movies/{id}` — Atualiza filme pelo ID
- `DELETE /api/v1/routes_movies/{id}` — Remove filme pelo ID

Consulte a documentação do Swagger para detalhes e exemplos.



## Observações

- Escrevi o código todo em ingles, por padrão pessoal.
- Adicionei rotas para Update e Delete (na descrição do desafio era obrigatório apenas rotas para retornar todos filmes | retornar um especifico | inserir), fiz dessa maneira para atender os requisitos de [C]reate [R]ead [U]pdate [D]elete. 
- Para dúvidas ou comentários, contate-me via email (jmpvboas@gmail.com) ou celular (+5535984325692).

---