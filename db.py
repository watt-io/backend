import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
engine = sqlalchemy.create_engine('sqlite:///filmes.db')
Base = declarative_base()

class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    titulo = Column(String(50), nullable=True)
    ano = Column(Integer(), nullable=True)
    genero = Column(String(15), nullable=True)


Session = sessionmaker(bind=engine)

def get_db():
    db = Session()
    try:
        yield db

    finally:
        db.close()
