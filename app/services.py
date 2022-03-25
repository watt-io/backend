import sqlalchemy.orm as _orm
import models as _models
import schemas as _schemas
import database as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_filme(db: _orm.Session, filme_id: int):
    return db.query(_models.Filme).filter(_models.Filme.id == filme_id).first()


def get_by_nome(db: _orm.Session, nome: str):
    return db.query(_models.Filme).filter(_models.Filme.nome == nome).first()


def get_filmes(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.Filme).offset(skip).limit(limit).all()


# fake_hashed_diretor = filme.diretor + "estediretornaoehvalido"
def create_filme(db: _orm.Session, filme: _schemas.FilmeCreate):
    db_filme = _models.Filme(nome=filme.nome, ano=filme.ano, diretor=filme.diretor)
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme
