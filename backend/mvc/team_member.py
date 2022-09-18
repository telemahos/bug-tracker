import re
import json
from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text
from sqlalchemy import desc


# Show All Team Member ##.order_by(desc('date'))
def team_member_get_all(db: Session, limit: int = 10, offset: int = 0 ):
    team_members = db.query(models.TeamMember).offset(offset).limit(limit).all()
    return team_members

# Show a Specific Team Member by project
def team_member_show_by_project(project_id:int, db: Session):
    team_members = db.query(models.TeamMember).filter(models.TeamMember.project_id == project_id).first()
    if not team_members:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Team Member in Project ID: {project_id} is not found')
    return team_members

# Show a Specific Team Member by date year: str, month: str,
# def team_member_show_by_date(year:str, month:str, db: Session, limit: int = 10, offset: int = 0 ):
#     # print(" TEST.....show_by_date22")
#     team = db.query(models.TeamMember).filter(models.TeamMember.date >= f'{year}-{month}-01', models.TeamMember.date <= f'{year}-{month}-31').all()
#     if not team:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Team by date: {year}-{month} is not found')
#     return team

# Show a Specific Team Members by id
def team_member_show(id: int, db: Session):
    team_member = db.query(models.TeamMember).filter(models.TeamMember.id == id).first()
    if not team_member:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Team with ID {id} is not found')
    return team_member

# Create and Post a new Team Member
def team_member_create(request: schemas.TeamMember, db: Session):
    new_team_member = models.TeamMember(project_id=request.project_id, user_id=request.user_id, team_role = request.team_role, assign_date = request.assign_date, active = request.active, note = request.note)
    db.add(new_team_member)
    db.commit()
    db.refresh(new_team_member)
    return new_team_member

def team_member_update(id: int, request: schemas.TeamMember, db: Session):
    update = db.query(models.TeamMember).filter(models.TeamMember.id == id).update({'user_id': request.user_id,'project_id': request.project_id, 'team_role': request.team_role, 'assign_date': request.assign_date, 'active': request.active, 'note': request.note})
    db.commit()
    return "Team Member updated!"

    
def team_member_destroy(id: int, db: Session):
    team_member = db.query(models.TeamMember).filter(models.TeamMember.id == id)
    if not team_member.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Team Member with id {id} is not found") 
    team_member.delete(synchronize_session=False)
    db.commit()
    return "Team Member deleted!"