from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hash import Hash
from . import JWTtoken

router = APIRouter(
    tags=['Authentication']
)

get_db = database.get_db

@router.post('/api/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")

    # Generate a JWT Token
    access_token = JWTtoken.create_access_token(
        # data={"sub": user.email} 
        data={"sub": user.name} 
    )

    return {"access_token": access_token, "token_type": "bearer"}

   