! API de Filmes - Desafio Técnico Backend

Rotas da API:

- `/filmes` - [GET] deve retornar todos os filmes cadastrados.
- `/filmes` - [POST] deve cadastrar um novo filme.
- `/filmes/{id}` -  [GET] deve retornar o filme com ID especificado.
- `/filmes/{id}` -  [DELETE] deve deletar o filme com ID especificado.
- `/filmes/{id}` -  [PUT] deve atualizar o filme com ID especificado.

#### Tecnologias

- Python 3.8
- [FastAPI]
- [Docker]
- [Docker-compose]
- [SQLAlchemy]
- [SQLite]

#### Como subir a aplicação?

- Faça o clone do repositório
- Execute o comando ``` docker-compose up -d ```
- Acesse a aplicação em <http://localhost:8000>
- Acesse a documentação da API em <http://localhost:8000/docs>
