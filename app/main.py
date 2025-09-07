from fastapi import FastAPI;
app = FastAPI(title="API de filmes")

from app.api import filme_routes
app.include_router(filme_routes.routes)


# Rodar o servidor: uvicorn main:app --reload
