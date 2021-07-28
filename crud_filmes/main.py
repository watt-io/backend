from fastapi import FastAPI
from . import models
from .database import engine
from .routers import filmes, user

app = FastAPI() 

models.Base.metadata.create_all(engine)

app.include_router(filmes.router)
app.include_router(user.router)