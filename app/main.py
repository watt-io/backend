from fastapi import FastAPI, HTTPException, Depends, status
from typing import Dict, Any
from sqlalchemy import Integer, String, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

url_db = "sqlite:///./filmes_db"
engine = create_engine(url_db,connect_args={"check_same_thread":False})
session_id = sessionmaker(autocommit=False, autoflush=False, bind = engine)
Base = declarative_base()

class Filme(Base):
    __tablename__ = "filmes"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    diretor = Column(String)
    
Base.metadata.create_all(bind=engine)

def get_session():
    db_connect = session_id()
    try: 
        yield db_connect
    finally:
        db_connect.close()
        
def initial_db():
    with session_id() as session_db:
        if not session_db.query(Filme).first():
            filmes_add = [
                Filme(titulo="Scarface", diretor="Brian de Palma"),
                Filme(titulo="Bastardos Inglórios", diretor = "Quentin Tarantino"),
                Filme(titulo="Interestelar", diretor="Christopher Nolan")
            ]
            session_db.add_all(filmes_add)
            session_db.commit()
            
initial_db()


@app.get("/Filmes")
def todos_filmes(db: Session=Depends(get_session)):
    todos_filme = db.query(Filme).all()
    return todos_filme

@app.get("/Filmes/{id}")
def filmes_id(id:int, db: Session = Depends(get_session)):
    filme_unico = db.query(Filme).filter(Filme.id==id).first()
    if not filme_unico: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")
    return filme_unico

@app.post("/Filmes")
def criar_filme(titulo:str, diretor:str, db: Session=Depends(get_session)):
    novo_filme = Filme(titulo=titulo, diretor=diretor)
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme
