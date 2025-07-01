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

4. **Cadastrar um filme**
Ao fazer uma requisição [POST] para `/filmes`, envie o seguinte JSON no corpo da requisição:

    ```json
    {
    "movie_name": "O Senhor dos Anéis: O Retorno do Rei",
    "synopsis": "Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar o olhar de Frodo e Sam quando eles se aproximam á Montanha da Perdição com o Um Anel.",
    "duration": 201,
    "year_release": 2003,
    "movie_gender": "Fantasia"
    }
    ```
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
