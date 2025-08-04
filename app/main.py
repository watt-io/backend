import logging
import sys

import uvicorn
from fastapi import FastAPI

from app.config import settings
from app.database import base, engine
from app.routers.filmes import router as filmes_router

base.metadata.create_all(bind=engine)

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG if settings.log_level == "DEBUG" else logging.INFO,
)

app = FastAPI(title=settings.project_name, docs_url="/docs")
app.include_router(filmes_router)


@app.get("/")
async def root():
    return {
        "message": "Olá WattIO! Bem-vindo à API backend.\nAcesse /docs para ver a documentação da API."
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
