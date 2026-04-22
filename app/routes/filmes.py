from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.filme import FilmeCreate, FilmeUpdate, FilmeResponse
from app.services.filme_service import FilmeService

router = APIRouter()

@router.get("/filmes", response_model=list[FilmeResponse])
def listar_filmes():
    db: Session = SessionLocal()
    try:
        return FilmeService.listar_filmes(db)
    finally:
        db.close()

@router.post("/filmes", response_model=FilmeResponse, status_code=201)
def cadastrar_filme(filme: FilmeCreate):
    db: Session = SessionLocal()
    try:
        return FilmeService.cadastrar_filme(db, filme)
    finally:
        db.close()

@router.get("/filmes/{id}", response_model=FilmeResponse)
def buscar_filme_por_id(id: int):
    db: Session = SessionLocal()
    try:
        return FilmeService.buscar_filme_por_id(db, id)
    finally:
        db.close()

@router.put("/filmes/{id}", response_model=FilmeResponse)
def atualizar_filme(id: int, dados_filme: FilmeUpdate):
    db: Session = SessionLocal()
    try:
        return FilmeService.atualizar_filme(db, id, dados_filme)
    finally:
        db.close()

@router.delete("/filmes/{id}")
def deletar_filme(id: int):
    db: Session = SessionLocal()
    try:
        return FilmeService.deletar_filme(db, id)
    finally:
        db.close()