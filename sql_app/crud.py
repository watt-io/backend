from select import select
from sqlalchemy.orm import Session

from . import models, schemas

class RepositorioFilmes():
    def __init__(self, db:Session):
        self.db = db

    def inserir(self, filme:schemas.Movie):# filme[variavel]:[tipo]
        db_movie = models.Movie(title=filme.title, 
                                descreption=filme.description)
        self.db.add(db_movie)
        self.db.commit()
        self.db.refresh(db_movie)
        return db_movie

    def consultar(self, movie_title: str):
         #stmt = select(models.Movie).filter_by(title=movie_title)
         #filme = self.db.execute(stmt).one()
        #filme = self.db.query(models.Movie).filter(models.Movie.title == movie_title).first()
        filme = self.db.query(models.Movie).filter(models.Movie.title == movie_title).first()
        return filme
    
    def exibir(self):
        filmes = self.db.query(models.Movie).all()
        return filmes
    




def get_movie(db: Session, movie_title: str):
    return db.query(models.Movie).filter(models.Movie.title == movie_title).first()

def get_movies(db: Session):
    return db.query(models.Movie).all()


def create_movie(db: Session, movie: schemas.Movie):
    db_movie = models.Movie(title=movie.title, description=movie.description)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie
