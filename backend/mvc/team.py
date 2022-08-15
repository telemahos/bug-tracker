import re
import json
from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text
from sqlalchemy import desc
# from fastapi_pagination import Page, pagination_params, page_size


# Show All issue ##.order_by(desc('date'))
def team_get_all(db: Session, limit: int = 10, offset: int = 0 ):
    team = db.query(models.Team).offset(offset).limit(limit).all()
    return team

# Show a Specific Team by project
def team_show_by_project(project_id:int, db: Session):
    team = db.query(models.Team).filter(models.Team.project_id == project_id).first()
    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Team in Project ID: {project_id} is not found')
    return team

# Show a Specific Team by date year: str, month: str,
# def team_show_by_date(year:str, month:str, db: Session, limit: int = 10, offset: int = 0 ):
#     # print(" TEST.....show_by_date22")
#     team = db.query(models.Team).filter(models.Team.date >= f'{year}-{month}-01', models.Team.date <= f'{year}-{month}-31').all()
#     if not team:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Team by date: {year}-{month} is not found')
#     return team

# Show a Specific Team by id
def team_show(id: int, db: Session):
    team = db.query(models.Team).filter(models.Team.id == id).first()
    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Team with ID {id} is not found')
    return team

# Create and Post a new Team
def team_create(request: schemas.Team, db: Session):
    new_team = models.Team(user_id=request.user_id, project_id = request.project_id, team_role = request.team_role, assign_date = request.assign_date, active = request.active, note = request.note)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team

def team_update(id: int, request: schemas.Team, db: Session):
    update = db.query(models.Team).filter(models.Team.id == id).update({'user_id': request.user_id,'project_id': request.project_id, 'team_role': request.team_role, 'assign_date': request.assign_date, 'active': request.active, 'note': request.note})
    db.commit()
    return "Team updated!"

    
def team_destroy(id: int, db: Session):
    team = db.query(models.Team).filter(models.Team.id == id)
    if not team.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Team with id {id} is not found") 
    team.delete(synchronize_session=False)
    db.commit()
    return "Team deleted!"