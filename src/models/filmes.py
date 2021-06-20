from typing import Optional, List
from enum import Enum

from sqlalchemy.sql.visitors import traverse_depthfirst
from src.models.core import IDModelMixin, CoreModel

class FilmeBase(CoreModel):
	tittle: Optional[str]

class FilmeCreate(FilmeBase):
	tittle: str

class FilmeInDB(IDModelMixin, FilmeBase):
	tittle: str

class FilmePublic(IDModelMixin, FilmeBase):
	pass