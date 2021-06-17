![WATTIO](http://wattio.com.br/web/image/1204-212f47c3/Logo%20Wattio.png)

#### Descrição

O desafio consiste em implementar um CRUD de filmes, utilizando [python](https://www.python.org/ "python") integrando com uma API REST e uma possível persistência de dados.

Rotas da API:

 - `/filmes` - [GET] deve retornar todos os filmes cadastrados.
 - `/filmes` - [POST] deve cadastrar um novo filme.
 - `/filmes/{id}` -  [GET] deve retornar o filme com ID especificado.

O Objetivo é te desafiar e reconhecer seu esforço para aprender e se adaptar. Qualquer código enviado, ficaremos muito felizes e avaliaremos com toda atenção!

#### Sugestão de Ferramentas 
Não é obrigatório utilizar todas as as tecnologias sugeridas, mas será um diferencial =]

- Orientação a objetos (utilizar objetos, classes para manipular os filmes)
- [FastAPI](https://fastapi.tiangolo.com/) (API com documentação auto gerada)
- [Docker](https://www.docker.com/) / [Docker-compose](https://docs.docker.com/compose/install/) (Aplicação deverá ficar em um container docker, e o start deverá seer com o comando ``` docker-compose up ```
- Integração com banco de dados (persistir as informações em json (iniciante) /[SqLite](https://www.sqlite.org/index.html) / [SQLAlchemy](https://fastapi.tiangolo.com/tutorial/sql-databases/#sql-relational-databases) / outros DB)


#### Como começar?

- Fork do repositório
- Criar branch com seu nome ``` git checkout -b feature/ana ```
- Faça os commits de suas alterações ``` git commit -m "[ADD] Funcionalidade" ```
- Envie a branch para seu repositório ``` git push origin feature/ana ```
- Navegue até o [Github](https://github.com/), crie seu Pull Request apontando para a branch **```main```**

#### Dúvidas?

Qualquer dúvida / sugestão / melhoria / orientação adicional só enviar email para hendrix@wattio.com.br

Salve!

# Resolução


### Documentação

[Documentação das Rotas da API via OpenAPI3](http://localhost/docs)

| Username | Password |
| -------- | -------- |
| admin  | admin  |

##### Build e execução dos containeres
```sh
docker-compose up --build -d
```

##### Execução dos testes iniciais(dentro do container)
```sh
cd /home/src/
pytest
```

##### Estrutura do .env no diretório /backend 

```sh
DEBUG=True
PROJECT_NAME=API Luiz
SECRET_KEY=l1d2b99ae9f502cd9bbb3c345337c0ca4e708b1c9e9fe1dbbcf30156c3630565a

MARIADB_USER=user
MARIADB_PASS=123456
MARIADB_HOST=db
MARIADB_DB=db

```