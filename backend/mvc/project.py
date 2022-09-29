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

# Create random Project Number
def get_project_nr():
  the_number=random.randint(101, 999)
  letters = string.ascii_uppercase
  the_letter = ''.join(random.choice(letters) for i in range(1))
  today = date.today()
  the_day = today.strftime("%d%m%y-")
  project_nr = str(the_day) + str(the_letter) + str(the_number)
  print("project_nr:", project_nr)
  return project_nr

# Show All Projects ##.order_by(desc('date'))
def project_get_all(db: Session, limit: int = 10, offset: int = 0 ):
    project = db.query(models.Project).offset(offset).limit(limit).all()
    return project

# Show a Specific Project by date year: str, month: str,
# def project_show_by_date(year:str, month:str, db: Session, limit: int = 10, offset: int = 0 ):
#     project = db.query(models.Project).filter(models.Project.date >= f'{year}-{month}-01', models.Project.date <= f'{year}-{month}-31').all()
#     return project

# Show a Specific Project by id
def project_show(id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Project with ID {id} is not found')
    return project

def project_create(request: schemas.Project, db: Session):
    new_project = models.Project(project_nr=get_project_nr(),start_date=request.start_date, due_date=request.due_date, title = request.title, description = request.description, tags = request.tags, active = request.active, status=request.status, priority = request.priority,  owner_id = request.owner_id)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

def project_update(id: int, request: schemas.Project, db: Session):
    db.query(models.Project).filter(models.Project.id == id).update({ 'start_date': request.start_date,"due_date": request.due_date,'title': request.title, 'description': request.description, 'tags': request.tags, 'active': request.active, 'status': request.status,  'priority': request.priority, 'owner_id': request.owner_id })
    db.commit()
    return "Project updated!"
    
def project_destroy(id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == id)
    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Project with id {id} is not found") 
    project.delete(synchronize_session=False)
    db.commit()
    return "Project deleted!"
