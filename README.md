# Desafio Backend Wattio

## Descrição
O desafio consiste em implementar um CRUD de filmes, utilizando python integrando com uma API REST e uma possível persistência de dados.

## Tecnologias utilizadas
**Linguagem:** Python 3.12.3<br>
**Framework:** FastAPI<br>
**Containerização:** Docker<br>

## Linha de raciocínio e orientações
- Desenvolvi a API com CRUD completo (Create, Read, Update e Delete), utilizando os princípios SOLID, mantendo uma arquitetura limpa e modular para a aplicação
- Arquitetura
    - Models (ORM de dados):  Define a estrtutura dos dados, com os campos e tipos
    - Schema (Pydantic): Define estrutura dos dados voltado para validação dos endpoints
    - Repository (Persistência): Camada que se conecta ao banco, persistindo os dados

- Criei um Seeder para popular o banco com alguns filmes para o teste

- Escrevi os endpoints em inglês, porém mais por costume e padronização

## Rotas desenvolvidas
 
- **GET** - /api/v1/movies -> Retorna a lista de todos os filmes cadastrados
- **GET** - /api/v1/movies/{movie_id} -> Retorna os dados de um filme específico pelo ID ou retorna 404 caso ele não seja encontrado
- **POST** - /api/v1/movies -> Cadastra um novo filme no banco
- **PUT** - /api/v1/movies/{movie_id} -> Atualiza um filme no banco pelo ID ou retorna 404 caso ele não exista
- **DELETE** - /api/v1/movies/{movie_id} -> Remove um filme do banco pelo ID ou retorna 404 caso ele não exista

## Variáveis de ambiente
Para as variáveis de ambiente eu criei o .env.example (docker compose puxará as informações dele), no nosso caso usaremos somente a URL para conexão com o banco de dados sendo **DATABASE_URL**.<br><br>
Ps: Já deixei configurado para utilizar o serviço do próprio docker compose, então já esta pronto para o teste (Não recomendado em produção, fiz apenas para o teste ser mais simples)

## Instalação e configuração local com Docker
Para utilizar o Docker, acesse a raiz do projeto e execute o comando abaixo:

Clone o repositório:
```bash
git clone git@github.com:daniel-guimaraess/backend-wattio.git
```

Execute o compose:
```bash
docker compose up
```

Feito isso, toda estrutura ja será preparada automaticamente, já subindo uma instância da API, sendo acessivel para teste com postman via:

http://127.0.0.1:8090

Utilizei o script **entrypoint.sh** para executar os comandos dentro do container, inclusive para inicialização do servidor, e também junto executo um script chamado **wait-for-it.sh**, pois com ele aguardo o banco de dados estar totalmente pronto, para que o backend suba, e não tenha erros de conexão, pois por mais que seja definida a variável **depends_on** no docker compose, ele não aguarda a inicialização completa do container.

## Instalação e configuração local sem docker
Para utilizar a API sem o container Docker, acesse a raiz do projeto e execute os comandos abaixo:

Altere .env.example para .env e configure com as informações do seu banco de dados

Clone o repositório:
```bash
git clone git@github.com:daniel-guimaraess/backend-wattio.git
```

**Criar ambiente virtual:**

```bash
python3 -m venv venv
```

**Ativar ambiente:**

```bash
source venv/bin/activate
```

**Instalar depedências:**

```bash
pip install -r requirements.txt
```

**Seeder para popular banco com filmes:**

```bash
python3 -m app.seeders.seed
```

**Iniciar servidor:**

```bash
uvicorn app.main:app --reload --port 8090
```
