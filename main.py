from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
import uvicorn
from models import Filme
from database import engine, Base, get_db
from repositories import FilmeRepository
from schemas import FilmeRequest, FilmeResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/filmes", response_model=FilmeResponse, status_code=status.HTTP_201_CREATED)
def create(request: FilmeRequest, db: Session = Depends(get_db)):

    filme = FilmeRepository.save(db,Filme(**request.dict()))

    return FilmeResponse.from_orm(filme)


@app.get('/filmes',response_model=list[FilmeResponse])
def fild_all(db: Session= Depends(get_db)):

    filmes = FilmeRepository.find_all(db)

    return [FilmeResponse.from_orm(filme) for filme in filmes]


@app.get('/filmes/{id}', response_model=FilmeResponse)
def find_by_id(id:int, db:Session = Depends(get_db)):

    filme = FilmeRepository.find_by_id(db,id)

    if not filme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado"
        )

    return FilmeResponse.from_orm(filme)


@app.delete('/filmes/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id:int, db:Session = Depends(get_db)):
    
    if not FilmeRepository.exist_by_id(db,id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "Filme não encontrado"
        )
    
    FilmeRepository.delete_by_id(db,id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/filmes/{id}', response_model=FilmeResponse)
def update(id:int,request:FilmeRequest, db:Session = Depends(get_db)):

    if not FilmeRepository.exist_by_id(db,id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "Filme não encontrado"
        )

    filme = FilmeRepository.save(db,Filme(id=id, **request.dict()))
    
    return FilmeResponse.from_orm(filme)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")