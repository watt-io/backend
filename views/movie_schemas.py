from pydantic import BaseModel

class Movie(BaseModel):

    title: str
    abstract: str
    genre: str
    main_actor: str
    director: str
    producion: str
    editions: str
    streaming: str
    price: int
    year: int