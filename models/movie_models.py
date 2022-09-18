import string
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
import uuid


from .db_conn.sqlite import Base, engine, metadata


class Movie(Base):
    __tablename__ = "movie"
    id = Column(String(60), primary_key=True )
    title = Column(String(60))
    abstract = Column(String(255))
    main_actor = Column(String(60))
    director = Column(String(60))
    producion = Column(String(60))
    editions = Column(String(60))
    streaming = Column(String(60))
    price = Column(Integer)
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




#########____CREATETABLE____###########

#Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)

