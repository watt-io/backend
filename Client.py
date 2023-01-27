from pydantic import BaseModel, Field

class Client(BaseModel): # Movie inherit from Base Model to future operations
        clientName : str = Field(min_length = 1, max_length = 100)
        clientPremium : bool
        clientAdress : str = Field(min_length = 1, max_length = 100)
