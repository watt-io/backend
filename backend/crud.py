from sqlalchemy.orm import Session

import models.model as model
import schemas.schema as schema


def get_movie_by_movie_id(db: Session, id: int):
    """
    Este método retorna um único filme busca por por ID
    :param db: database session object
    :param id: id only
    :return: data row if exist else None
    """
    return db.query(model.Movies).filter(model.Movies.id == id).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    """
    Este método retorna todos os filmes no DB
    :param db: database session object
    :param skip: numero de linhas a pular antes de incluir no resultado
    :param limit: especifica o número máximo de resultados a serem retornados
    :return: retorna todos os filmes no DB
    """
    return db.query(model.Movies).offset(skip).limit(limit).all()


def add_movie_details_to_db(db: Session, movie: schema.MovieAdd):
    """
    Este método insere filme no DB. commit e refresh 
    :param db: database session object
    :param movie: Object da classe schema.MovieAdd
    :return: a dictionary object of the record which has inserted
    """
    mv_details = model.Movies(
        movie_name=movie.movie_name,
        movie_year=movie.movie_year,
    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return model.Movies(**movie.dict())


def update_movie_details(db: Session, id: int, details: schema.UpdateMovie):
    """
    Este metodo atualiza dados pelo Id ja inserido anteriormente
    :param db: database session object
    :param id: id do registro ou Primary Key
    :param details: Objeto da classe schema.UpdateMovie
    :return: retorna o registro com o novo nome do filme
    """
    db.query(model.Movies).filter(model.Movies.id == id).update(vars(details))
    db.commit()
    return db.query(model.Movies).filter(model.Movies.id == id).first()


def delete_movie_details_by_id(db: Session, id: int):
    """
    Este metodo atualiza apaga registros pelo Id
    :param db: database session object
    :param id: id do registro ou Primary Key
    :return: None
    """
    try:
        db.query(model.Movies).filter(model.Movies.id == id).delete()
        db.commit()

    except Exception as e:
        raise Exception(e)
