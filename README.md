```
/app
  /models (SQLAlchemy para definicao dos schemas do DB)
  /repository (funcoes relativas a bancos de dados)
  /routers (endpoints da aplicação)
  /schemas (Classes pydantic para validacão de dados de entrada e sáida)
  /services (regras de negócio da aplicação)
  database.py
  config.py
  main.py
docker-compose.yaml
Dockerfile.yaml (configuracao para o container FastAPI)
.dockerignore (acelera transferencia de contexto)
.gitignore (arquivos que não vão para o repositório)
README.md
```

Para executar a aplicação você deve rodar no diretório raiz o seguinte comando:

```
docker compose -f 'docker-compose.yaml' up -d --build
```

Depois do comando acima você pode acessar http://localhost:8000/docs para visualizar a documentação da api, onde poderá realizar testes. Ou então pode usar o comando curl na linha de comando para realizar suas requisições.

Retornar todos os filmes cadastrados:

```bash
curl -X 'GET' \
  'http://localhost:8000/filmes/' \
  -H 'accept: application/json'
```

Cadastra um novo filme:

```bash
curl -X 'POST' \
  'http://localhost:8000/filmes/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "titulo": "string",
  "descricao": "string",
  "ano": 0,
  "genero": "string",
  "diretor": "string",
  "atores": [
    "string"
  ],
  "url_trailer": "https://example.com/",
  "classificacao_etaria": "string"
}'
```

Retorna o filme com ID especificado:

```bash
curl -X 'GET' \
  'http://localhost:8000/filmes/1' \
  -H 'accept: application/json'
```
