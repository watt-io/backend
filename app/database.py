from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATA_DIR = "/app/data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# sqlite, volume do Docker
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATA_DIR}/filmes.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# obter a sessão do bd em cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()