from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite3" #String de conexão com o DB

#Criação da engine
engine = create_engine(
  SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Classe de sessão o DB
SessaoLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Classe para crianção de classes de modelo
Base=declarative_base()

#função para disponibilizar instância da SessaoLocal
def get_db():
  db=SessaoLocal()
  try:
    yield db
  finally:
    db.close()