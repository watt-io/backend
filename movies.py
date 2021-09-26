from pydantic import BaseModel
from typing import Optional
class Movies(BaseModel):
    name : str
    year : Optional[int] = 0
    