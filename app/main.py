from fastapi import FastAPI
from app.api.v1.routes_movies import router as movies_router
from app.core.config import settings
from app.db.init_db import init_db

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

#Starts the database
init_db()

#Routes
app.include_router(movies_router, prefix="/api/v1/movies", tags=["Movies"])
