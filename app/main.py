from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Banco de dados
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Film(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    year = Column(Integer)

Base.metadata.create_all(bind=engine)

#FastAPI
app = FastAPI()

# Model para validar os dados recebidos nas requisições POST
class FilmCreate(BaseModel):
    title: str
    director: str
    year: int

# Rotas da API
@app.post("/filmes")
def create_film(film: FilmCreate):
    db = SessionLocal()
    db_film = Film(**film.dict())
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    db.close()
    return db_film

@app.get("/filmes")
def read_films():
    db = SessionLocal()
    films = db.query(Film).all()
    db.close()
    return films

@app.get("/filmes/{film_id}")
def read_film(film_id: int):
    db = SessionLocal()
    film = db.query(Film).filter(Film.id == film_id).first()
    db.close()
    if film is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return film