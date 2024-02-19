from sqlalchemy import Column, Integer, String
from db import get_db, Base

class Filmes(Base):
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
        filmes = db.query(Filmes).all()
        return filmes

    def buscarFilmes(filme_id: int, db):
        filme = db.query(Filmes).filter(Filmes.id == filme_id).first()
        return filme
    
    def atualizarFilme(filme_id:int, filme_mod, db):
        filme = db.query(Filmes).filter(Filmes.id == filme_id).first()
        if not filme:
            return {"erro": "Filme nao encontrado"}
        if filme_mod.titulo:
            filme.titulo = filme_mod.titulo
        if filme_mod.ano:
            filme.ano = filme_mod.ano
        if filme_mod.genero:
            filme.genero = filme_mod.genero
        db.commit()

    def deletarFilme(filme_id: int, db):
        filme = db.query(Filmes).filter(Filmes.id == filme_id).first() 
        db.delete(filme)
        db.commit()

    def to_json(self):
        return {"id": self.id, "titulo": self.titulo, "ano": self.ano, "genero": self.genero}    