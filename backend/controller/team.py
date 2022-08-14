from re import template
from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..mvc import case, user, project, team
# from fastapi_pagination import pagination_params, Page, paginate
# from fastapi_pagination.limit_offset import pagination_params

router = APIRouter(
    prefix="/api/team",
    tags=['Team']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowTeam]) 
async def all_team(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team.team_get_all(db)


@router.get('/{project_id}', response_model = List[schemas.ShowTeam], status_code=200)
async def show_team_by_project(project_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team.team_show_by_project(project_id, db)

@router.get('/{year}/{month}/', response_model = List[schemas.ShowTeam], status_code=200)
async def show_team_by_date(year: str, month: str , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team.team_show_by_date(year, month, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowTeam)
async def show_team(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team.team_show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_team(request: schemas.Team, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    print("CREATE TEAM CONTROLLER..............")
    return team.team_create(request, db)

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_team(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team.team_destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_team(id:int , request: schemas.Team, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team.team_update(id, request, db) 

