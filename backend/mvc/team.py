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

# Show a Specific Income by date year: str, month: str,
def team_show_by_date(year:str, month:str, db: Session, limit: int = 10, offset: int = 0 ):
    # print(" TEST.....show_by_date22")
    team = db.query(models.Team).filter(models.Team.date >= f'{year}-{month}-01', models.Team.date <= f'{year}-{month}-31').all()
    return team

# Show a Specific Income by id
def team_show(id: int, db: Session):
    team = db.query(models.Team).filter(models.Team.id == id).first()
    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Team with ID {id} is not found')
    return team

# Create and Post a new Income
def team_create(request: schemas.Team, db: Session):
    print("CREATE TEAM..............")
    new_team = models.Team(user_id=request.user_id, project_id = request.project_id, team_role = request.team_role, assign_date = request.assign_date, active = request.active, note = request.note)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    print("CREATE TEAM..............222222222")
    return new_team

