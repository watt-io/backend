![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

#### Descrição

CRUD de filmes, com autenticação de usuário.
Para cadastrar, obter ou excluir filmes, é necessário que o usuário esteja autenticado para que então seu acesso seja liberado.

##### Para acessar as rotas é necessário fazer a autentição!
Caso não queira realizar a autenticação comente a  variavel current_user passada como parâmetro nas funções presentes no arquivo
do seguinte caminho: crud_filmes\routers\filmes.py

Rotas da API:

 - `/filmes` - [GET] Retorna todos os filmes cadastrados.
 - `/filmes` - [POST] Cadastra um novo filme.
 - `/filmes/{id}` -  [GET] Retorna o filme com ID especificado.
 - `/filmes/{id}` -  [DEL] exclui o filme com ID especificado.

 - `/user` -  [POST] cria um novo usuário com nome, email e senha.
 - `/user/{id}` -  [GET] Retorna o usuário com a id especificada.

#### Ferramentas Utilizadas 

- Orientação a objetos (utilizar objetos, classes para manipular os filmes)
- [FastAPI](https://fastapi.tiangolo.com/) (API com documentação auto gerada)
- XXX
- XXX - [Docker](https://www.docker.com/) / [Docker-compose](https://docs.docker.com/compose/install/) (Aplicação deverá ficar em um container docker, e o start deverá seer com o comando ``` docker-compose up ``` - XXX
- XXX
- Integração com banco de dados (persistir as informações em [SqLite](https://www.sqlite.org/index.html) / [SQLAlchemy](https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases)


#### Dúvidas?

Qualquer dúvida / sugestão / melhoria / orientação adicional só enviar email para alysonhenrique26@gmail.com

Valeu!
