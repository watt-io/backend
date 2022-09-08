![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

#### Descrição

CRUD de filmes utilizando FastAPI, Docker e slqachemy

Rotas da API:

 - `/filmes` - [GET] Retorna todos os filmes cdastrados.
 - `/filmes` - [POST] Cadastra um novo filme
 - `/filmes/{id}` -  [GET] Retorna um filme a partir de um ID
 - `/filmes/{id}` -  [DELETE]Deleta um filme a partir de um ID

#### Arquivos

#### Requirements.txt
Arquivo txt onde possui todas as bibliotecas utilizadas na aplicação.

#### Dockerfile e docker-compose
Arquivos de configuração do Docker

#### db.py
Arquivo que faz conexão com o banco de dados, cria uma engine e instancia uma sessao local

#### models.py
Arquivo que cria o modelo Filmes para o banco de dados

#### repo.py
Arquivo que contém todos os métodos do CRUD

#### schema.py
Arquivo com a criação dos schemas do BD.

#### main.py
Arquivo que instancia o app e faz todas as requisições do CRUD.



#### COMO UPAR O APP
Primeiro, é necessario estar em um ambiente virtual.
Segundo, deve-se buildar a imagem no docker com o comando `docker-compose build`
terceiro, para iniciar deve-se rodar o comando `docker-compose up -d` e sua aplicação ja estrá dockerizada e rodando em um container.

#### Observações
A porta utilizada foi a 10000.
URL para acesso -> `http://127.0.0.1:10000/api/`
