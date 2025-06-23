from fastapi import FastAPI

from movies.routes import movies

app = FastAPI()

app.include_router(movies.router)
