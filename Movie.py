from pydantic import BaseModel, Field
from typing import Optional
from  Client import *

class MovieBase(BaseModel): 
        movieName : str = Field(min_length = 1, max_length = 100)
        movieLength : str = Field(min_length = 1, max_length = 100)
        movieGenre : str = Field(min_length = 1, max_length = 100)
        movieRelease : int
        
class Movie(MovieBase): 
        movieRentedBy : Optional[Client] = None # optional atributte
        
        class Config():
                orm_mode = True

