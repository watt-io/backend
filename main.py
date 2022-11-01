from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from modelos import Filme
from database import engine, Base, get_db
from repositorios import RepositorioFilme
from schemas import FilmeRequest, FilmeResponse

# Criação do DB e da tabela Filmes
Base.metadata.create_all(bind=engine)

app = FastAPI()

# rota de cadastro de filme


@app.post("/api/filmes", response_model=FilmeResponse, status_code=status.HTTP_201_CREATED)
def create(request: FilmeRequest, db: Session = Depends(get_db)):
    filme = RepositorioFilme.save(db, Filme(**request.dict()))
    return FilmeResponse.from_orm(filme)

# rota de listagem de filmes


@app.get("/api/filmes")
def find_all(db: Session = Depends(get_db)):
    filmes = RepositorioFilme.find_all(db)
    return [FilmeResponse.from_orm(filme) for filme in filmes]

# rota de busca de filme por id


@app.get("/api/filmes/{id}", response_model=FilmeResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    filme = RepositorioFilme.find_by_id(db, id)
    if not filme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado"
        )
    return FilmeResponse.from_orm(filme)

# rota de remoção de filme por id


@app.delete("/api/filmes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not RepositorioFilme.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado"
        )
    RepositorioFilme.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# rota de atualização de filme


@app.put("/api/filmes/{id}", response_model=FilmeResponse)
def update(id: int, request: FilmeRequest, db: Session = Depends(get_db)):
    if not RepositorioFilme.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado"
        )
    filme = RepositorioFilme.save(db, Filme(id=id, **request.dict()))
    return FilmeResponse.from_orm(filme)
