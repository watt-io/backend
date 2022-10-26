from fastapi import FastAPI
from routes.index import filme

app = FastAPI()

app.include_router(filme)