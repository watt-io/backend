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

### Documentação

#### Como iniciar a `API`

Abra o diretório do projeto e depois rode o seguinte comando:

```bash
docker-compose up
```

Ele vai fazer a build da imagem do `app`, baixar a imagem do `mongodb` e depois iniciar os containers, após isso está pronto para ser acessada em `http://0.0.0.0`, `http://localhost` ou `http://127.0.0.1`.

### Testar a aplicação

Para fazer os testes é necessário rodar o comando específicado em `Como iniciar a API`, e para testar utilizasse o comando:

```bash
docker exec backend_api pytest -vv .
```

Lembrando: é recomendado que você rode os testes sem ter adicionado nenhum filme novo no banco, pois isso pode quebrar o teste `test_retrieve_movies` dado que terá um valor diferente na hora da comparação.
