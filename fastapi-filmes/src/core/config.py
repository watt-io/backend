import os

class Settings:
    PROJECT_NAME: str = "FastAPI Filmes"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./films.db")

settings = Settings()
