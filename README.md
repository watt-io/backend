## Features

- é possivel realizar todas as operações CRUD na API

## Installation guide

- clone esse repositório
- instale o [Docker](https://www.docker.com/) / [Docker-compose](https://docs.docker.com/compose/install/)


## How to use

- utilize `docker-compose up`
- é possivel ver todos os endpoints em localhost:8000/docs
- pode-se utilizar [Postmand](EventsLogger.postman_collection.json) para a testagem, no repositório há um backup para importar

## API endpoints

<!--
    API endpoints: This will be a list of all created endpoints and expected responses.
 -->

### filmes

| HTTP Verbs | Endpoints          | Action                            |
| ---------- | ------------------ | --------------------------------- |
| GET        | /filmes            | listar todos os filmes     |
| GET        | /filmes            | buscar apenas um filme  |
| POST       | /filmes/{id}       | criar um novo filme |
| PUT        | /filmes/{id}       | atualizar um filme |
| DELETE     | /filmes/{id}       | deletar um filme |

## Technologies used

<!--
    Technologies used: This will list all the technologies the application is built with.
 -->

- [python](https://www.python.org/ "python")
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [FastAPI](https://fastapi.tiangolo.com/)


## Authors

<!--
    Authors: A list of authors and contributors to this project.
 -->

- [Lucas Oliveira](https://github.com/LordSouza)

## License

This project is available for use under the MIT License.
