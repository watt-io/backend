from pydantic import BaseModel, Field
from typing import Optional

class ClientBase(BaseModel): # Movie inherit from Base Model to future operations
        clientName : str = Field(min_length = 1, max_length = 100)
        clientPremium : bool
        clientAdress : str = Field(min_length = 1, max_length = 100)
        
        

class Client(ClientBase): 
        clientRentedMovieId : int
        
        class Config():
                orm_mode = True