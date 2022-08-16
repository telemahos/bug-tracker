from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..mvc import case, user, project

router = APIRouter(
    prefix="/api/project",
    tags=['Project']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowProject]) 
async def all_project(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return project.project_get_all(db)

# @router.get('/{year}/{month}/', response_model = List[schemas.ShowProject], status_code=200)
# async def show_project_by_date(year: str, month: str , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return project.project_show_by_date(year, month, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowProject)
async def show_project(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return project.project_show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_project(request: schemas.Project, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return project.project_create(request, db)

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_project(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return project.project_destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_project(id:int , request: schemas.Project, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return project.project_update(id, request, db) 

