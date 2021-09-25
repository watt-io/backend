from pydantic import BaseModel as bm
from pydantic import BaseModel

class Movies(BaseModel):
    name : str
    year : int
    id   : int
