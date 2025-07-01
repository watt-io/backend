![WATTIO](./img/banner-preview.png)

## Como executar a aplicação

Para executar a aplicação, siga os seguintes passos:

1.  **Pré-requisitos:**
    *   [Docker](https://www.docker.com/)
    *   [Docker Compose](https://docs.docker.com/compose/install/)

2.  **Clone o repositório:**
    ```bash
    git clone https://github.com/lucasaguiar-la/desafio-backend-wattio
    ```

3.  **Inicie a aplicação:**
    ```bash
    docker-compose up
    ```
A API estará disponível em `http://localhost:8000/`

---

#### Descrição

O desafio consiste em implementar um CRUD de filmes, utilizando [python](https://www.python.org/ "python") integrando com uma API REST e uma possível persistência de dados.

Rotas da API:

 - `/filmes` - [GET] deve retornar todos os filmes cadastrados.
 - `/filmes` - [POST] deve cadastrar um novo filme.
 - `/filmes/{id}` -  [GET] deve retornar o filme com ID especificado.

O Objetivo é te desafiar e reconhecer seu esforço para aprender e se adaptar. Qualquer código enviado, ficaremos muito felizes e avaliaremos com toda atenção!

#### Sugestão de Ferramentas 
Não é obrigatório utilizar todas as as tecnologias sugeridas, mas será um diferencial =]

- [x] Orientação a objetos (utilizar objetos, classes para manipular os filmes)
- [x] [FastAPI](https://fastapi.tiangolo.com/) (API com documentação auto gerada)
- [x] [Docker](https://www.docker.com/) / [Docker-compose](https://docs.docker.com/compose/install/) (Aplicação deverá ficar em um container docker, e o start deverá seer com o comando ``` docker-compose up ```
- [x] Integração com banco de dados (persistir as informações em json (iniciante) /[SqLite](https://www.sqlite.org/index.html) / [SQLAlchemy](https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases) / outros DB)

---
