from sqlalchemy.orm import Session

from models import Filme


class FilmeRepository:

# métodos do CRUD

    # retorna todos os filmes
    @staticmethod
    def findAll(db: Session) -> list[Filme]:
        return db.query(Filme).all()

    # cria um novo filme ou atualiza um filme existente
    @staticmethod
    def create(db: Session, filme: Filme) -> Filme:
        if filme.id:
            db.merge(filme)
        else:
            db.add(filme)
        db.commit()
        return filme

    # retorna um filme pelo id
    @staticmethod
    def findById(db: Session, id: int) -> Filme:
        return db.query(Filme).filter(Filme.id == id).first()

    # @staticmethod
    # def exists_by_id(db: Session, id: int) -> bool:
    #     return db.query(Filme).filter(Filme.id == id).first() is not None

    # deleta um filme pelo id
    @staticmethod
    def delete(db: Session, id: int) -> None:
        filme = db.query(filme).filter(filme.id == id).first()
        if filme is not None:
            db.delete(filme)
            db.commit()