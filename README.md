# Projeto Daniel Gustavo de Souza Rodrigues

Este README fornece instruções sobre como executar o projeto usando Docker Compose.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina antes de começar:

- Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## Como Executar

Execute o projeto usando o Docker Compose:
docker-compose up --build -d

Para parar e remover os contêineres, execute:
docker-compose down

Para remover os volumes também, utilize:
docker-compose down -v

# Acesso ao Projeto

O projeto deve estar disponível em http://localhost:80


# Exemplo de requisição

{
	"titulo": "Interestelar",
	"diretor": "Christopher Nolan",
	"genero": "Ficção Científica",
	"ano": 2014
}
