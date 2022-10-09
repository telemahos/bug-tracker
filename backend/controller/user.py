from re import template
from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..mvc import user

router = APIRouter(
    prefix="/api/user",
    tags=['User']
)

get_db = database.get_db

""" USER"""
@router.get('/', response_model=List[schemas.ShowUser]) 
async def all_users(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.user_get_all(db)

@router.post('/', response_model=schemas.ShowUser)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_user(id:int , request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.user_update(id, request, db) 

@router.get('/{id}', response_model=schemas.ShowUser)
async def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.get('/{email}', response_model=schemas.ShowUser)
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return user.user_by_email(email, db)