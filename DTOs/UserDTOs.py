from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=30, description="Nome de usuário (3-30 caracteres)")
    email: EmailStr = Field(..., description="E-mail do usuário")
    is_active: bool = Field(default=True, description="Usuário está ativo?")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=128, description="Senha do usuário (mínimo 6 caracteres)")

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
