from pydantic import BaseModel
from typing import Optional
class Filme(BaseModel):
    id: Optional[int] = None
    titulo: str
    diretor: str
    ano: int