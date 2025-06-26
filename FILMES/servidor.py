
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import tabelas, dados, repositorio
from app.infra import engine, SessionLocal

tabelas.Base.metadata.create_all(bind=engine)
app = FastAPI(title="CRUD de Filmes")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/filmes", response_model=list[dados.FilmeOut])
def listar(db: Session = Depends(get_db)):
    return repositorio.buscar_todos(db)

@app.get("/filmes/{filme_id}", response_model=dados.FilmeOut)
def obter(filme_id: int, db: Session = Depends(get_db)):
    filme = repositorio.buscar_por_id(db, filme_id)
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme

@app.post("/filmes", response_model=dados.FilmeOut)
def criar(filme: dados.FilmeCreate, db: Session = Depends(get_db)):
    return repositorio.criar(db, filme)

@app.put("/filmes/{filme_id}", response_model=dados.FilmeOut)
def atualizar(filme_id: int, filme: dados.FilmeCreate, db: Session = Depends(get_db)):
    filme_atualizado = repositorio.atualizar(db, filme_id, filme)
    if not filme_atualizado:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme_atualizado

@app.delete("/filmes/{filme_id}")
def deletar(filme_id: int, db: Session = Depends(get_db)):
    sucesso = repositorio.remover(db, filme_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return {"mensagem": "Filme removido com sucesso"}
