# Filmes API

Esta é uma API desenvolvida em Python com o framework FastAPI, projetada para gerenciar informações sobre filmes. A aplicação utiliza um banco de dados SQLite para armazenar os dados e pode ser executada em um ambiente Docker.

## Recursos da API

A API suporta as seguintes operações:

- **Listar todos os filmes**: `GET /Filmes`
- **Obter detalhes de um filme pelo ID**: `GET /Filmes/{id}`
- **Adicionar um novo filme**: `POST /Filmes`

## Requisitos

Certifique-se de ter instalado os seguintes componentes:

- [Python 3.9+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)

## Instalação e Execução do Projeto

1. Clone este repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd WATTIO-TESTE
```

2. Construa e inicie os containers Docker:

```bash
docker-compose up --build
```

3. Acesse a documentação interativa da API no navegador:

```
http://localhost:8000/docs
```

4. As rotas da API estão detalhadas abaixo:

### Listar todos os filmes

**Requisição:**

```bash
GET /Filmes
```

**Resposta:**

```json
[
  {
    "id": 1,
    "titulo": "Scarface",
    "diretor": "Brian de Palma"
  },
  {
    "id": 2,
    "titulo": "Bastardos Inglórios",
    "diretor": "Quentin Tarantino"
  }
]
```

### Obter detalhes de um filme pelo ID

**Requisição:**

```bash
GET /Filmes/{id}
```

**Resposta:**

```json
{
  "id": 1,
  "titulo": "Scarface",
  "diretor": "Brian de Palma"
}
```

### Adicionar um novo filme

**Requisição:**

```bash
POST /Filmes
```

**Corpo da Requisição:**

```json
{
  "titulo": "Matrix",
  "diretor": "Lana Wachowski e Lilly Wachowski"
}
```

**Resposta:**

```json
{
  "id": 4,
  "titulo": "Matrix",
  "diretor": "Lana Wachowski e Lilly Wachowski"
}
```

