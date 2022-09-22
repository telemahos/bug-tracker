import re
import string
import random
from datetime import date
import json
from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text
from sqlalchemy import desc


# Create the Case Number
def get_case_nr():
  the_number=random.randint(10121, 89999)
  letters = string.ascii_uppercase
  the_letter = ''.join(random.choice(letters) for i in range(1))
  today = date.today()
  the_day = today.strftime("%d%m%y-")
  case_nr = str(the_day) + str(the_letter) + str(the_number)
  print("case_nr:", case_nr)
  return case_nr

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

# Show Cases by status
def case_show_by_status(status: int, db: Session, limit: int = 10, offset: int = 0 ):
    case = db.query(models.Case).filter(models.Case.status == status).all()
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Case withe the status ID: {status} is not found')
    return case

# Show a Specific Case by id
def case_show(id: int, db: Session):
    case = db.query(models.Case).filter(models.Case.id == id).first()
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Case with ID {id} is not found')
    return case

# Create and Post a new Case
def case_create(request: schemas.Case, db: Session):
    print("+++++++++new_case: ")
    new_case = models.Case(case_nr=get_case_nr(),start_date=request.start_date, due_date=request.due_date,title = request.title, description = request.description, tags = request.tags, status = request.status, priority = request.priority, case_type = request.case_type, project_id = request.project_id, owner_id = request.owner_id)
    # print("new_case: " + new_case)
    db.add(new_case)
    db.commit()
    db.refresh(new_case)
    return new_case

def case_update(id: int, request: schemas.Case, db: Session):
    db.query(models.Case).filter(models.Case.id == id).update({'case_nr': get_case_nr(), 'start_date': request.start_date, 'due_date': request.due_date, 'title': request.title, 'description': request.description, 'tags': request.tags, 'status': request.status, 'priority': request.priority, 'case_type': request.case_type, 'project_id': request.project_id, 'owner_id': request.owner_id})
    db.commit()
    return "Case updated!"

    
def case_destroy(id: int, db: Session):
    case = db.query(models.Case).filter(models.Case.id == id)
    if not case.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Case with id {id} is not found") 
    case.delete(synchronize_session=False)
    db.commit()
    return "Case deleted!"