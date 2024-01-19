from sqlalchemy import Column, Integer, String
from database import Base, get_db


class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    genero = Column(String, index=True, nullable=True)
    ano = Column(Integer, index=True, nullable=True)
    descricao = Column(String, index=True, nullable=True)

    def criar(filme, db):
        db.add(filme)
        db.commit()
        db.refresh(filme)

    def listar(db):
        filmes = db.query(Filme).all()
        return filmes

    def buscar(filme_id: int, db):
        filme = db.query(Filme).filter(Filme.id == filme_id).first()
        if not filme:
            return "Filme não encontrado!"
        return filme

    def atualizar(filme_id: int, filme_modificado, db):
        filme = db.query(Filme).filter(Filme.id == filme_id).first()
        if not filme:
            return {"error": "Filme não encontrado!"}
        if filme_modificado.nome:
            filme.nome = filme_modificado.nome
        if filme_modificado.ano:
            filme.ano = filme_modificado.ano
        if filme_modificado.genero:
            filme.genero = filme_modificado.genero
        if filme_modificado.descricao:
            filme.descricao = filme_modificado.descricao
        db.commit()

    def deletar(filme_id: int, db):
        filme = db.query(Filme).filter(Filme.id == filme_id).first()
        db.delete(filme)
        db.commit()

    def __repr__(self):
        return f"<Filme {self.nome}>"
