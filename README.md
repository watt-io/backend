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


#### Como Rodar? (Quem sou eu para te ensinar, mas vamos lá)

- Clone o repositório
- Navegue até a pasta raiz do projeto
- No Prompt de Comando rode o comando  ``` docker-compose up ```
- Agora já pode acessar o endereço ``` http://127.0.0.1:8000/docs ``` e testar minha aplicação :)
- Obs: Eu criei duas rotas adicionais. Uma para atualizar um filme que já existe, e outra para deletar um filme pelo ID.
- Obs2: Quando criar um filme novo, o parâmetro "cast" recebe uma lista. No endereço ``` http://127.0.0.1:8000/docs ``` o método "Save Item" possui uma caixa na qual você pode escrever um lista para o parâmetro 'cast'
