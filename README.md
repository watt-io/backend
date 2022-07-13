## Biblioteca de Filmes - RESTful API

## Requisitos
- `Docker`
- `docker compose`

### Como usar?

1 - Clone o respositório localmente:
```git
git clone -b feature/gabriel https://github.com/GabrielSousa02/backend.git
```

2 - Entre na pasta do projeto:
```bash
cd ./backend
```

3 - Execute o comando:
```bash
docker compose up -d
```

4 - Em seguida, precisamos executar as migrações no banco de dados - SQLite, ainda na pasta raiz do projeto:
```bash
docker compose exec django_api python manage.py migrate
```

5 - Pronto, o projeto já está rodando no endereço:
```bash
http://localhost:8000
```