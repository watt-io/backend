

## Resolução do Desafio de implementação de um CRUD de filmes

##

O desafio consiste em implementar um CRUD de filmes, utilizando [python](https://www.python.org/ "python") integrando com uma API REST e uma possível persistência de dados.

Rotas da API:
 - `/` - [GET] retorna a quantidade de filmes disponiveis.
 - `/filmes` - [GET] retorna todos os filmes cadastrados.
 - `/filmes` - [POST] cadastra um novo filme.
 - `/filmes/{id}` -  [GET] retorna o filme com ID especificado.
 - `/filmes/{id}` - [PUT] atualiza um filme com ID especificado.
 - `/filmes/{id}` - [DELETE] apaga um filme com ID especificado.
 - `/alugar/{id}` - [POST] cadastra um cliente e atribui a ID de um filme especificado.
 - `/Devolver/{id}` - [DELETE] apaga um cliente de acordo com a ID de um filme especificado.
 - `/clientes` - [GET] retorna todos os clientes cadastrados.
 - `/clientes/filmes` - [GET] retorna os filmes alugados, ou seja indisponíveis.

##

Foi desenvolvido uma aplicação, para que um ambiente de uma locadora de filmes fosse simulado. É possível o cadastro, consulta, edição e remoção de __filmes__, além da capacidade do cadastro de __clientes__ para o Aluguel das obras.

Para o funcionamento dessa aplicação, algumas configurações devem ser feitas inicialmente. Deve-se ter em mente que as seguintes ferramentas foram usadas nesse projeto

- [python](https://www.python.org/ "python") 3.11.1
- [FastAPI](https://fastapi.tiangolo.com/) 0.89.1 / [uvicorn](https://www.uvicorn.org/) 0.20.0
- [SQLite](https://www.sqlite.org/index.html) 3.40.1 / [SQLAlchemy](https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases) 2.0.0

Para Python deve-se ir até o [site oficial](https://www.python.org/) e depois em dowloads para adquirir o instalador. Abrindo o arquivo e seguindo os passos, facilmente a ferramenta ficará disponível para uso.

Para o FastAPI e uvicorn é possível consultar a documentação no [site oficial](https://fastapi.tiangolo.com/), que ensina a instalação. Mas basicamente é necessário a realização de dois comandos no prompt para as ferramentas estarem funcionando corretamente:

> pip install fastapi

> pip install "uvicorn[standard]"

Por fim o SQLite deve será adquirido no [site oficial](https://www.sqlite.org/index.html) seguindo para dowload e baixando o arquivo _sqlite-tools_ para Windows. Agora a instalação do SQLAchemy é possível através do prompt digitando o comando:

> pip install sqlalchemy

Agora todas as ferramentas estão configuradas para o funcionamento da aplicação. Para que o server seja lançado deve se ir até a pasta de instalação desse projeto e digitar o seguinte comando:

> uvicorn main:app --reload

O comando irá retornar um link para o acesso do usuário a API:

![Link API](/assets/Screenshot_uvicorn.png)

Ao acessar o link uma página no navagador será aberta na rota base da API, para uma maior noção das funcionabilidades disponíveis basta acessar a documentação auto gerada pela API, que pode ser acessada por __"Link API"/docs.__

