from sqlalchemy import Column, Integer, String, Float
import uuid


from .db_conn.sqlite import Base, metadata, engine

class Movie(Base):
    __tablename__ = "movie"
    id = Column(String(60), primary_key=True, default=uuid.uuid4)
    title = Column(String(60))
    abstract = Column(String(255))
    genre = Column(String(60))
    main_actor = Column(String(60))
    director = Column(String(60))
    producion = Column(String(60))
    editions = Column(String(60))
    streaming = Column(String(60))
    price = Column(Float)
    year = Column(Integer)
    
    def getMovies(self):
        return {
            "id": self.id,
            "title": self.title
        }
    
    def getById(self):
        return {
            "id": self.id,
            "title": self.title,
            "abstract": self.abstract,
            "main_actor": self.main_actor,
            "director": self.director,
            "production": self.producion,
            "edition": self.editions,
            "streaming": self.streaming,
            "price": self.price,
            "year": self.year
        }
    
if (Base):
    pass
    Base.metadata.create_all(engine)
    