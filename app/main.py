from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import engine
from app.routers import auth, filmes


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(
    title="API de Filmes",
    description=(
        "CRUD de filmes com FastAPI, PostgreSQL e Docker. "
        "Autentique-se em POST /auth/token e use o token Bearer nas rotas /filmes."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth.router)
app.include_router(filmes.router)
