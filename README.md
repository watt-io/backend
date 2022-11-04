![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

#### Descrição

Teste para vaga de desenvolvedor backend.
Foi implementado um CRUD de filmes, utilizando [python](https://www.python.org/ "python") integrando com uma API REST e persistindo os dados em um banco de dados SQLite.

Rotas da API:

 - `/filmes` - [GET] deve retornar todos os filmes cadastrados.
 - `/filmes` - [POST] deve cadastrar um novo filme.
 - `/filmes/{id}` -  [GET] deve retornar o filme com ID especificado.
 - `/filmes/{id}` - [PUT] deve atualizar o filme com ID especificado.
 - `/filmes/{id}` - [DELETE] deve deletar o filme com ID especificado.

 #### Como startar o projeto

    - Clone o projeto
    - Rodar o comando `docker-compose up` na raiz do projeto
    - Acesse o endereço `http://localhost:8000/docs` para ver a documentação da API

