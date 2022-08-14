import re
import json
from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.sql import text
from sqlalchemy import desc
# from fastapi_pagination import Page, pagination_params, page_size


# Show All issue ##.order_by(desc('date'))
def case_get_all(db: Session, limit: int = 10, offset: int = 0 ):
    case = db.query(models.Case).offset(offset).limit(limit).all()
    return case

# Show a Specific Case by date year: str, month: str,
def case_show_by_date(year:str, month:str, db: Session, limit: int = 10, offset: int = 0 ):
    case = db.query(models.Case).filter(models.Case.date >= f'{year}-{month}-01', models.Case.date <= f'{year}-{month}-31').all()
    return case

# Show Cases by project
def case_show_by_project(project_id: int, db: Session, limit: int = 10, offset: int = 0 ):
    case = db.query(models.Case).filter(models.Case.project_id == project_id).all()
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Case from the Project with ID {project_id} is not found')
    return case

# Show Cases by User
def case_show_by_owner(owner_id: int, db: Session, limit: int = 10, offset: int = 0 ):
    case = db.query(models.Case).filter(models.Case.owner_id == owner_id).all()
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Case from the User with ID {owner_id} is not found')
    return case

# Show Cases by Case Type
def case_show_by_case_type(case_type: int, db: Session, limit: int = 10, offset: int = 0 ):
    case = db.query(models.Case).filter(models.Case.case_type == case_type).all()
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Case withe the Case ID: {case_type} is not found')
    return case

# Show Cases by Priority
def case_show_by_priority(priority: int, db: Session, limit: int = 10, offset: int = 0 ):
    case = db.query(models.Case).filter(models.Case.priority == priority).all()
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Case from the User with ID {priority} is not found')
    return case

# Show Cases by active
def case_show_by_active(active: int, db: Session, limit: int = 10, offset: int = 0 ):
    case = db.query(models.Case).filter(models.Case.active == active).all()
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Case withe the active ID: {active} is not found')
    return case

# Show a Specific Case by id
def case_show(id: int, db: Session):
    case = db.query(models.Case).filter(models.Case.id == id).first()
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Case with ID {id} is not found')
    return case

# Create and Post a new Case
def case_create(request: schemas.Case, db: Session):
    new_case = models.Case(date=request.date, title = request.title, body = request.body, tags = request.tags, active = request.active, priority = request.priority, case_type = request.case_type, project_id = request.project_id, owner_id = request.owner_id)
    db.add(new_case)
    db.commit()
    db.refresh(new_case)
    return new_case

def case_update(id: int, request: schemas.Case, db: Session):
    update = db.query(models.Case).filter(models.Case.id == id).update({'date': request.date,'title': request.title, 'body': request.body, 'tags': request.tags, 'active': request.active, 'priority': request.priority, 'case_type': request.case_type, 'project_id': request.project_id, 'owner_id': request.owner_id})
    db.commit()
    return "Case updated!"

    
def case_destroy(id: int, db: Session):
    case = db.query(models.Case).filter(models.Case.id == id)
    if not case.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Case with id {id} is not found") 
    case.delete(synchronize_session=False)
    db.commit()
    return "Case deleted!"