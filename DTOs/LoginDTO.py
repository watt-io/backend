from pydantic import BaseModel, Field, EmailStr

class LoginUser(BaseModel):
    email: EmailStr = Field(..., description="E-mail do usuário")
    password: str = Field(..., min_length=6, max_length=128, description="Senha do usuário (mínimo 6 caracteres)")
