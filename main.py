from fastapi import FastAPI
import uvicorn
from app.routers import filmes_routers
from app.db.database import *


# Criando as tabelas no banco de dados, se não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def pagina_inicial():
    return {"Olá FastAPI": "Olá FastAPI"}


# Configurando as rotas com o modulo filmes_routers
app.include_router(filmes_routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
