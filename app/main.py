from fastapi import FastAPI
from app.api import movies
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Filmes API")

Base.metadata.create_all(bind=engine)

app.include_router(movies.router)
