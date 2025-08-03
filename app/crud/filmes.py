from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.filme import Movie
from app.schemas.filme import MovieCreate, MovieUpdate


class CRUDMovie:

    def get(self, db: Session, movie_id: int) -> Optional[Movie]:
        return db.query(Movie).filter(Movie.id == movie_id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[Movie]:
        return db.query(Movie).offset(skip).limit(limit).all()

    def create(self, db: Session, movie: MovieCreate) -> Movie:
        db_movie = Movie(**movie.dict())
        db.add(db_movie)
        db.commit()
        db.refresh(db_movie)
        return db_movie

    def update(
        self, db: Session, movie_id: int, movie_update: MovieUpdate
    ) -> Optional[Movie]:
        db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
        if db_movie:
            update_data = movie_update.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_movie, field, value)
            db.commit()
            db.refresh(db_movie)
        return db_movie

    def delete(self, db: Session, movie_id: int) -> bool:
        db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
        if db_movie:
            db.delete(db_movie)
            db.commit()
            return True
        return False

    def get_by_title(self, db: Session, title: str) -> Optional[Movie]:
        return db.query(Movie).filter(Movie.title == title).first()

    def get_by_genre(
        self, db: Session, genre: str, skip: int = 0, limit: int = 100
    ) -> List[Movie]:
        return (
            db.query(Movie)
            .filter(Movie.genre == genre)
            .offset(skip)
            .limit(limit)
            .all()
        )


movie_crud = CRUDMovie()
