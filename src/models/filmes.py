from typing import Optional
from enum import Enum
from src.models.core import IDModelMixin, CoreModel

class FilmeBase(CoreModel):
	tittle: Optional[str]

class FilmeCreate(FilmeBase):
	tittle: str

class FilmeInDB(IDModelMixin, FilmeBase):
	name: str

class FilmePublic(IDModelMixin, FilmeBase):
	pass