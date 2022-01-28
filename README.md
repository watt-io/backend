<h1 align="center">
    CRUD de filmes - Python
</h1>
<h4 align="center">
    Teste backend da Inowatt
</h4>

**Dev:** [Vinícius Zamariola](https://github.com/Zamariolo)
**Vaga:** Estagíario de backend

Contato:

<a href="https://www.linkedin.com/in/vin%C3%ADcius-zamariola/">
  <img align="left" alt="Abhishek's Discord" width="22px" src="https://cdn-icons-png.flaticon.com/512/174/174857.png" />
</a>

<a href="mailto:viniciuszamariola@gmail.com">
  <img align="left" alt="Abhishek's Discord" width="22px" src="https://cdn-icons-png.flaticon.com/512/281/281769.png" />
</a>
<br>
<hr />

CRUD de filmes com informações de nota do [IMDB](https://www.imdb.com/) e se é recomendado para todas as idades feito em Python com persistência de informações em banco de dados SQLite.

#### Ferramentas utilizadas

- Python POO
- [FastAPI](https://fastapi.tiangolo.com/)
- Banco de dados [SQLite](https://www.sqlite.org/index.html) manipulado via [SQLAlchemy](https://www.sqlalchemy.org/)
- Ambiente virtual venv
- [uvicorn](https://www.uvicorn.org/) (como servidor)
- [pydantic](https://pydantic-docs.helpmanual.io/) (Para validação de dados)

Acabei não utilizando o Docker :/

#### Modelagem de dados

Colunas:

- **id:** Chave primária e única identificador do filme `int`
- **nome:** Nome do filme `str`
- **nota_imdb:** Nota do Filme no [IMDB](https://www.imdb.com/) `float`
- **family_friendly:** Se o filme é recomendado para todas as idades `bool`

#### Subindo a API

1. Acessar a branch `git checkout feature/vinicius-zamariola`

2. Ativar o ambiente virtual `source environment/bin/activate`

3. Inicializar a API/servidor via uvicorn `uvicorn main:app` ou em modo de desenvolvimento `uvicorn main:app --reload`

4. Armazenar novos filmes e consultar os filmes registrados no ip gerado na porta `:8000` =)

5. Documentação em `<ip-da-aplicacao>/docs` ou `<ip-da-aplicacao>/redoc`

#### Funcionalidades

- Validação de tipos de dados
- Validação se a nota no imdb está no range esperado (0-10) ao inserir novo filme

- Rotas:
  - `/estoufuncionando` - [GET] Verifica se a API esta funcionando retornando 'sim'
  - `/filmes` - [GET] retorna todos os filmes cadastrados.
  - `/filmes` - [POST] cadastra um novo filme.
  - `/filmes/{id}` - [GET] retorna o filme com ID especificado.

#### Obrigado!

- Vinícius Zamariola

<hr />

#### Todo-list para melhorar este projeto

- [ ] Implementar imagem docker
- [ ] Inserir testes automatizados (TDD)
- [ ] Rota para deletar filmes
- [ ] Rota para atualizar filmes

#### Exemplos de resposta e payloads

**Rota**: `get /estoufuncionando`
Response:

```json
"sim"
```

**Rota**: `get /filmes`
Response:

```json
[
  { "nota_imdb": 7.8, "id": 1, "nome": "Avatar", "family_friendly": true },
  { "nota_imdb": 7.8, "id": 2, "nome": "Titanic", "family_friendly": true }
]
```

**Rota**: `get /filmes/1`
Response:

```json
  { "nota_imdb": 7.8, "id": 1, "nome": "Avatar", "family_friendly": true }
```

**Rota**: `post /filmes/`:
Payload:

```json
  { "nome": "Avatar", "nota_imdb": 7.8, "family_friendly": true }
```

Response:
```json
  { "id": X, "nome": "Avatar", "nota_imdb": 7.8, "family_friendly": true }
```

