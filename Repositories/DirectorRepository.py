from sqlalchemy.orm import Session
from Models.DirectorModel import Director
from DTOs.DirectorDTOs import DirectorCreate

class DirectorRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, director_data: DirectorCreate) -> Director:
        director = Director(**director_data.dict())
        self.db.add(director)
        self.db.commit()
        self.db.refresh(director)
        return director

    def list_all(self, skip: int = 0, limit: int = 10, name: str | None = None):
        query = self.db.query(Director)
        if name:
            query = query.filter(Director.name == name)
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, director_id: int):
        return self.db.query(Director).filter(Director.id == director_id).first()

    def update(self, director_id: int, director_data: DirectorCreate):
        director = self.get_by_id(director_id)
        if director:
            for field, value in director_data.dict().items():
                setattr(director, field, value)
            self.db.commit()
            self.db.refresh(director)
        return director
        
    def delete(self, director_id: int):
        director = self.get_by_id(director_id)
        if director:
            self.db.delete(director)
            self.db.commit()
        return director
