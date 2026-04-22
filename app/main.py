from fastapi import FastAPI
from app.database.connection import Base, engine
from app.models.filme import Filme
from app.routes.filmes import router as filmes_router

app = FastAPI(title="API de Filmes - WATTIO")

Base.metadata.create_all(bind=engine)

app.include_router(filmes_router)

@app.get("/")
def home():
    return {"Teste API Filmes"}