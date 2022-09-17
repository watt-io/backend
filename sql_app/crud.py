from sqlalchemy.orm import Session

from models import Movie

class MovieRepository:
 
    def find_all(db: Session) -> list[Movie]:
        return db.query(Movie).all()

    
    def save(db: Session, movie: Movie) -> Movie:
        db.add(movie)
        db.commit()
        return movie

    
    def find_by_title(db: Session, movie: Movie) -> Movie:
        return db.query(Movie).filter(Movie.titulo == movie.titulo).first()

    
    def find_by_id(db: Session, id: int) -> Movie:
        return db.query(Movie).filter(Movie.id == id).first()
    