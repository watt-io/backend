### Sobre a API

A API, desenvolvida com FASTAPI e pymongo, possui nove rotas:
- ```/filmes``` - [GET] retorna todos os filmes do banco de dados
- ```/filmes/{id}``` - [GET] retorna o filme com a id {id}
- ```/filmes/``` - [POST] adiciona um filme ao banco de dados
- ```/filmes/{id}``` - [PUT] altera informações sobre um filme no banco de dados
- ```/filmes/{id}``` - [DELETE] remove o filme de id {id} do banco de dados

- ```/generos``` - [GET] retorna todos os generos do banco de dados
- ```/generos``` - [POST] adiciona um gênero ao banco de dados
- ```/generos/{id}``` - [PUT] altera informações sobre um gênero no banco de dados
- ```/generos/{id}``` - [DELETE] remove o gênero de id {id} do banco de dados

Atualmente ela roda apenas localmente. Para rodá-la, basta abrir a pasta do repositório e executar os seguintes comandos:
- ```pip install -r requirements.txt``` - para instalar os pacotes necessários
- ```cd src``` - para entrar na pasta do código fonte
- ```uvicorn main:app``` 

### Sobre o Banco de Dados

O Banco de Dados escolhido para esse desafio foi o MongoDB, principalmente pela possibilidade de acesso à nuvem. A API possui conexão constante e aberta ao banco de dados. Apesar de tal abordagem não ser recomendada pelos riscos à segurança do banco, optei visando a facilidade de observação do mesmo. O banco de dados conta com quatro tabelas:
- Control - Tabela de controle que visa quantificar e facilitar o controle dos filmes e gêneros
- Filmes - Tabela dos filmes; arquiva os seguintes dados: [ID], [Título], [Duração] e [Link]
- Generos - Tabela dos gêneros; arquiva os seguintes dados: [ID] e [Nome]
- FilmesGeneros - Tabela que arquiva a relação entre os filmes e generos