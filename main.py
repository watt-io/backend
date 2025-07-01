from fastapi import FastAPI
from src.controller import movie_controller

app = FastAPI()

app.include_router(movie_controller.router)

@app.get('/')
def root():
    return {
        'Status': 'API rodando...'
    }