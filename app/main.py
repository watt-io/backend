# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List

app = FastAPI()


POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "password"
POSTGRES_DB = "testdb"
POSTGRES_HOST = "db"  
POSTGRES_PORT = "5432"

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
Base = declarative_base()

class Filme(Base):
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    diretor = Column(String)
    genero = Column(String)
    ano = Column(Integer)


def create_database(engine):
    Base.metadata.create_all(bind=engine)

create_database(engine)


class FilmeCreate(BaseModel):
    titulo: str
    diretor: str
    genero: str
    ano: int

class FilmeResponse(BaseModel):
    id: int
    titulo: str
    diretor: str
    genero: str
    ano: int

@app.post("/filmes/", response_model=FilmeResponse)
def create_filme(filme: FilmeCreate):
    db = SessionLocal()
    db_filme = Filme(**filme.dict())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    response_filme = FilmeResponse(**db_filme.__dict__)
    db.close()
    return response_filme

@app.get("/filmes/", response_model=List[FilmeResponse])
def read_filmes(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    filmes = db.query(Filme).offset(skip).limit(limit).all()
    db.close()
    
    response_filmes = [FilmeResponse(**filme.__dict__) for filme in filmes]

    return response_filmes


@app.get("/filmes/{filme_id}", response_model=FilmeResponse)
def read_filme(filme_id: int):
    db = SessionLocal()
    filme = db.query(Filme).filter(Filme.id == filme_id).first()
    db.close()
    if filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    response_filme = FilmeResponse(**filme.__dict__)

    return response_filme
