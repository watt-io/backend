from pydantic import BaseModel

class home(BaseModel):
    messge: str
    time_request: str
    status: str
    content: object
    footer: str
    info: str
    author: str
    