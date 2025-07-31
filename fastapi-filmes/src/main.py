from fastapi import FastAPI
from src.api import router
from src.db import Base, engine

app = FastAPI(title="API Filmes")

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "API Filmes rodando!"}
