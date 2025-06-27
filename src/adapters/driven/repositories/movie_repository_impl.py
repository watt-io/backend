from typing import Optional
from core.ports.movie_interface import MovieInterface
from core.models.movie import Movie
from adapters.driven.database.connection import SessionLocal
from adapters.driven.database.models import MovieORM

class SQLAlchemyMovieRepository(MovieInterface):
    def add(self, movie: Movie) -> None:
        db = SessionLocal()
        db_movie = MovieORM(
            id=movie.id,
            title=movie.title,
            year=movie.year,
            duration=movie.duration
        )
        db.add(db_movie)
        db.commit()
        db.close()

    def list(self):
        db = SessionLocal()
        movies = db.query(MovieORM).all()
        db.close()
        return [Movie(id=m.id, title=m.title, year=m.year, duration=m.duration) for m in movies]

    def get_by_id(self, movie_id: str):
        db = SessionLocal()
        m = db.query(MovieORM).filter(MovieORM.id == movie_id).first()
        db.close()
        if m:
            return Movie(id=m.id, title=m.title, year=m.year, duration=m.duration)
        return None

    def get_by_title(self, title: str):
        db = SessionLocal()
        m = db.query(MovieORM).filter(MovieORM.title == title).first()
        db.close()
        if m:
            return Movie(id=m.id, title=m.title, year=m.year, duration=m.duration)
        return None

    def delete_by_title(self, title: str) -> int:
        db = SessionLocal()
        deleted_count = db.query(MovieORM).filter(MovieORM.title == title).delete()
        db.commit()
        db.close()
        return deleted_count

    def update(self, movie: Movie) -> Optional[Movie]:
        db = SessionLocal()
        db_movie = db.query(MovieORM).filter(MovieORM.id == movie.id).first()
        if db_movie:
            db_movie.title = movie.title
            db_movie.year = movie.year
            db_movie.duration = movie.duration
            db.commit()
            updated = Movie(id=db_movie.id, title=db_movie.title, year=db_movie.year, duration=db_movie.duration)
            db.close()
            return updated
        db.close()
        return None