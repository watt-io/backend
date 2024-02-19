from sqlalchemy import Column, Integer, String
from db import get_db, Base

class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    titulo = Column(String(50), nullable=True)
    ano = Column(Integer(), nullable=True)
    genero = Column(String(15), nullable=True)

    def criarFilme(filme, db):
        db.add(filme)
        db.commit()
        db.refresh(filme)

    def listarFilmes(db):    
        filmes = db.query(Filme).all()
        return filmes

    def buscarFilmes(filme_id: int, db):
        filme = db.query(Filme).filter(Filme.id == filme_id).first()
        return filme
    
    def atualizarFilme(filme_id:int, filme_modificado, db):
        filme = db.query(Filme).filter(Filme.id == filme_id).first()
        if not filme:
            return {"erro": "Filme nao encontrado"}
        if filme_modificado.titulo:
            filme.titulo = filme_modificado.titulo
        if filme_modificado.ano:
            filme.ano = filme_modificado.ano
        if filme_modificado.genero:
            filme.genero = filme_modificado.genero
        db.commit()

    def deletarFilme(filme_id: int, db):
        filme = db.query(Filme).filter(Filme.id == filme_id).first() 
        db.delete(filme)
        db.commit()