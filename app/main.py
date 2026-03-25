from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app.models import Base, Filme
from app.schemas import FilmeCreate, FilmeUpdate, FilmeResponse

# Inicializa as tabelas do banco
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Filmes",
    description="API para gerenciamento de catálogo de filmes",
    version="1.0.0"
)



@app.get("/filmes", response_model=list[FilmeResponse], tags=["Filmes"])
def listar_filmes(
    genero: str | None = Query(None, description="Filtrar por gênero"),
    diretor: str | None = Query(None, description="Filtrar por diretor"),
    ano: int | None = Query(None, description="Filtrar por ano de lançamento"),
    skip: int = Query(0, ge=0, description="Pular registros"),
    limit: int = Query(10, ge=1, le=100, description="Limite de resultados"),
    db: Session = Depends(get_db),
):
    """Lista todos os filmes com filtros e paginação."""
    query = db.query(Filme)

    if genero:
        query = query.filter(Filme.genero.ilike(f"%{genero}%"))
    if diretor:
        query = query.filter(Filme.diretor.ilike(f"%{diretor}%"))
    if ano:
        query = query.filter(Filme.ano == ano)

    return query.offset(skip).limit(limit).all()


@app.post("/filmes", response_model=FilmeResponse, status_code=201, tags=["Filmes"])
def criar_filme(filme: FilmeCreate, db: Session = Depends(get_db)):
    """Cadastra um novo filme."""
    novo_filme = Filme(**filme.model_dump())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme


@app.get("/filmes/{id}", response_model=FilmeResponse, tags=["Filmes"])
def buscar_filme(id: int, db: Session = Depends(get_db)):
    """Busca um filme pelo ID."""
    filme = db.query(Filme).filter(Filme.id == id).first()
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme


@app.put("/filmes/{id}", response_model=FilmeResponse, tags=["Filmes"])
def atualizar_filme(id: int, dados: FilmeUpdate, db: Session = Depends(get_db)):
    """Atualiza um filme existente."""
    filme = db.query(Filme).filter(Filme.id == id).first()
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")

    dados_atualizados = dados.model_dump(exclude_unset=True)
    if not dados_atualizados:
        raise HTTPException(status_code=400, detail="Nenhum dado informado")

    for campo, valor in dados_atualizados.items():
        setattr(filme, campo, valor)

    db.commit()
    db.refresh(filme)
    return filme


@app.delete("/filmes/{id}", status_code=204, tags=["Filmes"])
def deletar_filme(id: int, db: Session = Depends(get_db)):
    """Remove um filme pelo ID."""
    filme = db.query(Filme).filter(Filme.id == id).first()
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")

    db.delete(filme)
    db.commit()


