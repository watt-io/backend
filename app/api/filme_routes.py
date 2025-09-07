from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import filme_schema
from app.crud import filme_crud
from app.db.session import get_db

routes = APIRouter(prefix="/filmes", tags=['Filmes'])

@routes.get('/', response_model=list[filme_schema.FilmeOut])
async def getFilmes(db: Session = Depends(get_db)):
    """
    Rota padrão para listagem de filmes.
    """
    return filme_crud.get_filme(db)

@routes.post('/', response_model=filme_schema.FilmeOut)
async def createdFilmes(filme: filme_schema.FilmeCreate, db: Session = Depends(get_db)):
    """
    Rota padrão para a criação de filmes.
    """
    return filme_crud.create_filme(db, filme)

@routes.get(f"/{id}", response_model=filme_schema.FilmeOut)
async def getFilmeById(id: int, db: Session = Depends(get_db)):
    """
    Rota padrão para a obter um filme pelo seu ID
    """
    return filme_crud.get_filme_by_id(db, id)