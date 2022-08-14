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
    db.query(models.Case).filter(models.Case.id == id).update({'title': request.title, 'body': request.body})
    # db.query(models.Case).filter(models.Case.id == id).update(dict({'date': request.date, 'title': request.title, 'body': request.body, 'tags': request.tags, 'active': request.active, 'priority': request.priority, 'case_type': request.case_type, 'project_id': request.project_id, 'owner_id': request.owner_id}))
    # update = db.query(models.Case).filter(models.Case.id == id)
    # db.add(update)
    # update.update(request.dict())
    db.commit()
    db.refresh()
    return case_update

    # query = text("""UPDATE blogs SET date=:date, title=:title, body=:body, tags=:tags, active=:active  WHERE id = :id""").params(date=request.date, title=request.title, body=request.body, tags= request.tags, active= request.active, id=id)
    # result = db.execute(query)
    # if not result:
    #     raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The post with id {id} is not found')
    # db.commit()
    # return request

# Update an Case
# def case_update(id: int, request: schemas.Case, db: Session):
#     query = text("""UPDATE cases SET date=:date, service_income_1=:service_income_1, service_income_2=:service_income_2, bar_income_1=:bar_income_1, bar_income_2=:bar_income_2, pos=:pos, z_count=:z_count, vat=:vat, waitress_1=:waitress_1, waitress_2=:waitress_2, barman_1=:barman_1, barman_2=:barman_2, notes=:notes, shift_id=:shift_id WHERE id = :id""").params( date=request.date, service_income_1 = request.service_income_1, service_income_2 = request.service_income_2, bar_income_1=request.bar_income_1, bar_income_2=request.bar_income_2, pos=request.pos, z_count=request.z_count, vat=request.vat, waitress_1=request.waitress_1, waitress_2=request.waitress_2, barman_1=request.barman_1, barman_2=request.barman_2, notes=request.notes, shift_id=request.shift_id , id=id)
#     result = db.execute(query)
#     if not result:
#         raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The income with id {id} is not found')
#     db.commit()
#     return request

# Delete an Income
def issue_destroy(id: int, db: Session):
    income = db.query(models.Income).filter(models.Income.id == id)
    if not income.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The income with id {id} is not found") 
    income.delete(synchronize_session=False)
    db.commit()
    return "deleted!"