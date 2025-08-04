from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://wattio:wattio@localhost/wattiodb"
    project_name: str = "Wattio Backend"
    log_level: str = "DEBUG"

    class Config:
        env_file = ".env"


settings = Settings()
