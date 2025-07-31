from sqlalchemy.orm import Session
from src.schemas import FilmCreate
from src.models.film import FilmModel

class FilmService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_films(self):
        return self.db.query(FilmModel).all()

    def create_film(self, film_create: FilmCreate):
        film = FilmModel(**film_create.dict())
        self.db.add(film)
        self.db.commit()
        self.db.refresh(film)
        return film
    
    def get_film(self, id: int):
        return self.db.query(FilmModel).filter(FilmModel.id == id).first()
