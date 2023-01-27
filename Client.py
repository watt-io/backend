from pydantic import BaseModel

class Client(BaseModel): # Movie inherit from Base Model to future operations
        clientName : str
        clientPremium : bool
        clientAdress : str
