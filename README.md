![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)



#### Descrição

O desafio consiste em implementar um CRUD de filmes, utilizando [python](https://www.python.org/ "python") integrando com uma API REST e uma possível persistência de dados.

Rotas da API:

 - `/filmes` - [GET] deve retornar todos os filmes cadastrados.
 - `/filmes` - [POST] deve cadastrar um novo filme.
 - `/filmes/{id}` -  [GET] deve retornar o filme com ID especificado.
 - `/filmes/{id}` -  [DELETE] deve excluir um filme pelo ID especificado.
 - `/filmes/{id}` -  [PUT] deve atualizar um filme pelo ID especificado e o campo que desejado.


#### Manual de uso
**Para usuários com Docker instalado no computador**:

    Basta utilizar o comando ``` sudo docker-compose up ```!

**Para usuários sem Docker instalado no computador**:

    Primeiramente, você deverá instalar duas bibliotecas ``` pip install fastapi ``` e ``` pip install uvicorn ```. Após isso, será necessário ir até o diretório onde o arquivo ``` app_api.py ``` está localizado, logo após será necessário digitar o seguinte comando no terminal ``` uvicorn app_api:app --reload ```.

