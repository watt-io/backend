
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from starlette import status
from .. import schemas, database, models, hashing, token
from sqlalchemy.orm import Session

Hash = hashing.Hash

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="Invalid credentials!")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="Incorrect password")
    
    # gera um chave jwt e retorna
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}