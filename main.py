from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine) #instância do db
app = FastAPI()

def get_db():     
    db = SessionLocal()     
    try:         
        yield db     
    finally:
        db.close()

#----------------------CADASTRA FILME-----------------------------------
@app.post("/filmes", response_model = schemas.Filme) 
def cadastra_filme(filme: schemas.Filme, db: Session = Depends(get_db)):
    db_filme = crud.get_filme_by_id(db, filme.id) 

    if db_filme:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "Esse filme já foi cadastrado"
            )
    return crud.cria_filme(db=db, filme = filme) #retorna objeto Filme

#--------------------RETORNA FILME BY ID---------------------------------
@app.get("/filmes/{filme_id}", response_model = schemas.Filme)
def retorna_filme(filme_id: int, db: Session = Depends(get_db)):
    db_filme = crud.get_filme_by_id(db, filme_id)
    
    if db_filme is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Nenhum filme encontrado"
            )
    return db_filme 

#--------------------RETORNA TODOS FILMES---------------------------------
@app.get('/filmes', response_model = schemas.lista)
def retorna_todos_filmes(db: Session = Depends(get_db)):
    db_filmes = crud.get_filmes(db) #retorna db de Filme
    
    lista_filmes = []
    for filme in db_filmes:
        lista_filmes.append(filme) #add filmes do bd em uma lista vazia
    return lista_filmes        
