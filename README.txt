# API de Filmes - Backend

Este projeto contém uma API simples para gerenciar filmes.

## Como Rodar a API (com Docker)

1.  **Pré-requisitos:** Tenha o [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e rodando.
2.  **No Terminal:** Abra o terminal na pasta raiz do projeto (`backend`).
3.  **Construa a imagem:**
    ```bash
    docker compose build
    ```
4.  **Inicie a API:**
    ```bash
    docker compose up
    ```
    (Para rodar em segundo plano, use `docker compose up -d`)

## Acessando a API

Após iniciar a API, abra seu navegador e vá para [http://localhost:8000/docs](http://localhost:8000/docs) para ver e testar a documentação.

## Endpoints da API

* **`GET /filmes`**: Lista todos os filmes.
* **`GET /filmes/{id}`**: Pega detalhes de um filme pelo ID.
* **`POST /filmes`**: Adiciona um novo filme. (Precisa de um JSON no corpo da requisição com `titulo`, `ano`, `genero`).