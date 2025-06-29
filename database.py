from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho do banco de dados
DATABASE_URL = "sqlite:///./filmes.db"

# Cria o engine de conexão com SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Cria uma sessão com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()