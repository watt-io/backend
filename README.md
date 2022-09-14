# Desafio API Filmes CRUD

![PostmanPrint](https://github.com/LewisDamy/FilmesAPI_backend/blob/main/PrintScreen%20Postman.png)

#### Descrição

O desafio consiste em implementar um CRUD de filmes, utilizando [python](https://www.python.org/ "python") integrando com uma API REST e uma possível persistência de dados.

Rotas da API:

 - `/filmes` - [GET] retorna todos os filmes cadastrados.
 - `/filmes` - [POST] cadastra um novo filme.
 - `/filmes/{id}` -  [GET] retorna o filme com ID especificado.
 - `/filmes/{id}` -  [PUT] atualiza o filme com ID especificado.
 - `/filmes/{id}` -  [DELETE] deleta o filme com ID especificado.

#### Ferramentas Utilizadas
- [Django](https://www.djangoproject.com)
- [Django Rest Framework](https://www.django-rest-framework.org)
- [Docker](https://www.docker.com/)

#### Como utilizar?
-   Faça o download do arquivo zip ou rode ```git clone '[Link do Repositorio]'```
-   Dentro do folder em que contem o Makefile execute ```make install``` para fazer a instalação dos requisitos
-   Em seguida execute ```make migration```
-   Para construir o Dockerfile localmente ```make build```
-   Executando o docker ```make run```

Agora é só acessar a pagina http://127.0.0.1:8000/ pela web ou apps como [Postman](https://www.postman.com)
    