from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text
from ..hash import Hash


# Show All issue ##.order_by(desc('date'))
def user_get_all(db: Session, limit: int = 10, offset: int = 0 ):
    users = db.query(models.User).offset(offset).limit(limit).all()
    return users

def create(request: schemas.User, db:Session):
    new_user = models.User(name=request.name, email=request.email, user_role= request.user_role, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The User with ID {id} is not found')
    return user