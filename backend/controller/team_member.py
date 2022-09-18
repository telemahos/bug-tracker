from re import template
from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..mvc import case, user, project, team_member

router = APIRouter(
    prefix="/api/team_member",
    tags=['Team Member']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowTeamMember]) 
async def all_team_member(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team_member.team_member_get_all(db)


@router.get('/project/{project_id}', response_model = schemas.ShowTeamMember, status_code=200)
async def show_team_by_project(project_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team_member.team_member_show_by_project(project_id, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowTeamMember)
async def show_team(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team_member.team_member_show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_team(request: schemas.TeamMember, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team_member.team_member_create(request, db)

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_team(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team_member.team_member_destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_team_member(id:int , request: schemas.TeamMember, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return team_member.team_member_update(id, request, db) 

