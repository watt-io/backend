import os


class Config:
    DATABASE_URL = os.getenv(
        'A-POSTGRES_DATABASE_URL', 'postgresql+asyncpg://filmes:filmes@db:5432/filmes')

