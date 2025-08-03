from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Movies API"
    PROJECT_VERSION: str = "1.0.1"
    DATABASE_URL: str = "sqlite:///./movies.db"

    class Config:
        env_file = ".env"

settings = Settings()
