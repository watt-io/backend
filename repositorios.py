from sqlalchemy.orm import Session
from modelos import Filme


class RepositorioFilme:
    # busca todos os filmes cadastrados
    @staticmethod
    def find_all(db: Session) -> list[Filme]:
        return db.query(Filme).all()

    # cadastra ou edita um filme
    @staticmethod
    def save(db: Session, filme: Filme) -> Filme:
        if filme.id:
            db.merge(filme)
        else:
            db.add(filme)
        db.commit()
        return Filme

    # busca um filme com base no id
    @staticmethod
    def find_by_id(db: Session, id: int) -> Filme:
        return db.query(Filme).filter(Filme.id == id).first()

    # verifica se um filme existe com base no id
    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Filme).filter(Filme.id == id).first() is not None

    # exclui um filme com base no id
    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        filme = db.query(Filme).filter(Filme.id == id).first()
        if filme is not None:
            db.delete(filme)
            db.commit()
