from pydantic import BaseModel
class Movies(BaseModel):
    name : str
    year : int
    