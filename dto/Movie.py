from json import JSONEncoder
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class Movie(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    year: int
    director: str
    genre: List[str]
    imdb: float


# Dealing with no UUID serialization support in json
JSONEncoder_olddefault = JSONEncoder.default


def JSONEncoder_newdefault(self, o):
    if isinstance(o, UUID):
        return str(o)
    return JSONEncoder_olddefault(self, o)


JSONEncoder.default = JSONEncoder_newdefault
