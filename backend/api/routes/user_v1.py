from datetime import datetime
from fastapi import APIRouter, Depends
from .auth_v1 import get_current_user
from pydantic import BaseModel

router = APIRouter()


class UserOut(BaseModel):
    id: int
    username: str
    inserted_on: datetime


@router.get('/me', response_model=UserOut)
async def read_users_me(current_user=Depends(get_current_user)):
    """
    Return current user info
    """
    return current_user
