# Instruções para rodar o projeto

Para rodar o projeto é necessário ter instalado o docker e docker-compose, feito isso basta rodar o comando `docker-compose up` no root do projeto e sua API estará rodando.

A API possui as seguintes rotas:
- GET http://127.0.0.1:8000/movies/
- GET http://127.0.0.1:8000/movies/{movie_id}
- POST http://127.0.0.1:8000/movies/

Para acessar a documentação do projeto, com a aplicação rodando acesse o link http://127.0.0.1:8000/docs