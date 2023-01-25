from fastapi import FastAPI # importando o framework para uso da API

# criação da API (rodar através do comando uvicorn [nome do arquivo]:[nome do objeto] --reload)
app = FastAPI()

# definição de rotas para determinar a funcionalidade da aplicação

@app.get("/")
def homePage():
    return 'Hello world'

