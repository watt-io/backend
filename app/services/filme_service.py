from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.filme import Filme
from app.schemas.filme import FilmeCreate, FilmeUpdate


class FilmeService:
    @staticmethod
    def listar_filmes(db: Session):
        return db.query(Filme).all()

    @staticmethod
    def buscar_filme_por_id(db: Session, id: int):
        filme = db.query(Filme).filter(Filme.id == id).first()

        if filme is None:
            raise HTTPException(status_code=404, detail="Filme não encontrado")

        return filme

    @staticmethod
    def cadastrar_filme(db: Session, filme: FilmeCreate):
        novo_filme = Filme(
            titulo=filme.titulo,
            diretor=filme.diretor,
            ano=filme.ano,
            genero=filme.genero
        )

        db.add(novo_filme)
        db.commit()
        db.refresh(novo_filme)

        return novo_filme

    @staticmethod
    def atualizar_filme(db: Session, id: int, dados_filme: FilmeUpdate):
        filme = db.query(Filme).filter(Filme.id == id).first()

        if filme is None:
            raise HTTPException(status_code=404, detail="Filme não encontrado")

        filme.titulo = dados_filme.titulo
        filme.diretor = dados_filme.diretor
        filme.ano = dados_filme.ano
        filme.genero = dados_filme.genero

        db.commit()
        db.refresh(filme)

        return filme

    @staticmethod
    def deletar_filme(db: Session, id: int):
        filme = db.query(Filme).filter(Filme.id == id).first()

        if filme is None:
            raise HTTPException(status_code=404, detail="Filme não encontrado")

        db.delete(filme)
        db.commit()

        return {"mensagem": "Filme removido com sucesso"}