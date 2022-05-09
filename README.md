#### Descrição

Uma API REST de um CRUD de filmes implementado em python com o docker, o fastapi e o banco de dados SqLite.

Rotas da API:

 - `/filmes` - [GET] retorna uma lista de filmes, filtrando por qualquer parâmetro(titulo, diretor, pais, ano, censura, sinopse), caso não receba nenhum parâmetro, retorna uma lista com todos os filmes do banco.
 - `/filmes` - [POST] cadastra um novo filme.
 - `/filmes/{id}` -  [GET] retorna o filme com ID especificado.
 - `/filmes/{id}` -  [PATCH] permite atualizar os dados de um filme com um ID especificado.
 - `/filmes/{id}` -  [DELETE] deve excluir o filme com ID especificado.

Observações: O banco de dados possui mais de 6000 filmes, devido a isso o fastiapi demora a retornar todos eles. Caso esse erro ocorra basta acessar no navegador o `localhost:8000/filmes` que irá entregar a lista mais rapidamente.


#### Arquivos em Python

 - `models.py` - Faz a criação do banco de dados e dos modelos utilizados na API para criação e manipulação das tabelas.
 - `create.py` - Acessa o arquivo csv e insere no banco todos os que são filmes com seus respectivos dados.
 - `main.py`- Implementação de todos as funções de manipulação da API.


#### Upando a aplicação
 
 MAQUINA COM DOCKER INSTALADO:
    -Basta realizar no terminar o comando `docker compose up`.
    -Após isso basta acessar no navegador o `localhost:8000/docs` para acessar o fastapi.

 MAQUINA SEM DOCKER INSTALADO:
    - Primeiramente é necessária a instalaçao de um compilador de pyhton.
    - Após isso é necessário instalar todos os pacotes listados em requirements.txt, utilize o comando `pip install nomeDoPacote` para realizar a instalação.
    - No terminal execute os arquivos em python na seguinte ordem:
        1º models.py
        2º create.py
        Os comandos podem variar de acordo com a versão do compilador instalado na sua máquina.
    - Execute o seguinte comando no terminal `py -m uvicorn main:app --reload` ou `python -m uvicorn main:app --reload` dependendo da versão do seu compilador.
    - Por fim, acesse `http://127.0.0.1:8000/docs` em seu navegador para acessar o fastapi.