# FastAPI com MySQL

Este é um projeto de exemplo de uma API com FastAPI e persistência em um banco de dados MySQL.

## Inicialização com Docker

Para inicializar o projeto com docker, execute os comandos abaixo na raiz do projeto:
```bash
docker compose build
docker compose up
```
Após 15 segundos, a aplicação deverá estar rodando.

## Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação FastAPI.
- `controllers/`: Contém os controladores da API.
- `models/`: Define os modelos de dados e interfaces de repositório.
- `services/`: Contém serviços auxiliares, como a conexão com o banco de dados.
- `utils/`: Inclui utilitários, como a configuração do banco de dados.
- `docker-compose.yml`: Arquivo de configuração para o Docker Compose.
- `Dockerfile`: Define como a imagem Docker é construída.

## Variáveis de Ambiente

Certifique-se de definir as variáveis de ambiente necessárias no arquivo `.env` antes de executar o build do projeto:

- `MYSQL_USER`: Usuário do banco de dados MySQL. (padrão: `root` (não recomendado em produção, ajustar docker-compose))
- `MYSQL_PASSWORD`: Senha do banco de dados MySQL. (padrão: `root` (não recomendado em produção, ajustar docker-compose))
- `MYSQL_DATABASE`: Nome do banco de dados a ser utilizado. (padrão: `filmesDB`)
- `DB_TYPE`: Tipo de banco de dados (`mysql` é a única implementação atualmente).

## Testando a API

Após iniciar o projeto, você pode acessar a documentação interativa da API em `http://localhost:8000/docs`.

## Finalizando o Projeto

Para parar e remover os contêineres do Docker, utilize o comando:

```bash
docker compose down
```
```

