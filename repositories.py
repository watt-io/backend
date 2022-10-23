from sqlalchemy.orm import Session
from models import Filme

class FilmeRepository:
    @staticmethod
    def find_all(db:Session) -> list[Filme]:
        return db.query(Filme).all()

    @staticmethod
    def save(db: Session, filme:Filme) -> Filme:
        db.add(filme)
        db.commit()
        return filme

    @staticmethod
    def find_by_id(db: Session, id: int) -> Filme:
        return db.query(Filme).filter(Filme.id == id).first()

    @staticmethod
    def exist_by_id(db: Session, id: int):
        return db.query(Filme).filter(Filme.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id:int):
        filme = db.query(Filme).filter(Filme.id == id).first()

        if filme is not None:
            db.delete(filme)
            db.commit()
