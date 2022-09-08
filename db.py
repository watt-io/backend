from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Conexão com o banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"

#Criação da engine de conexão
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Criação da sessão local com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    #Instânciando a sessão local
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
