from fastapi import FastAPI
from . import models, database
from .routes import router

# Criação das tabelas no banco
models.Base.metadata.create_all(bind=database.engine)

# Instância da aplicação
app = FastAPI(title="CRUD de Filmes 🎬")

# Inclusão das rotas
app.include_router(router)

# Rota raiz para evitar erro 404
@app.get("/")
def home():
    return {"mensagem": "API de Filmes 🎬 - acesse /docs para ver a documentação"}

# Executa apenas se rodar diretamente com python main.py
if __name__ == "__main__":
    import uvicorn
    print("Swagger disponível em: http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)
