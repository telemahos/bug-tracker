import re
import json
from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.sql import text
from sqlalchemy import desc
# from fastapi_pagination import Page, pagination_params, page_size


# Show All issue ##.order_by(desc('date'))
def issue_get_all(db: Session, limit: int = 10, offset: int = 0 ):
    issue = db.query(models.Issue).offset(offset).limit(limit).all()
    # issue = db.query(models.Issue).filter(models.Issue.date >= "2021-09-01", models.Issue.date <= "2021-09-31").all()
    return issue

# Show a Specific Income by date year: str, month: str,
def issue_show_by_date(year:str, month:str, db: Session, limit: int = 10, offset: int = 0 ):
    # print(" TEST.....show_by_date22")
    issue = db.query(models.Issue).filter(models.Issue.date >= f'{year}-{month}-01', models.Issue.date <= f'{year}-{month}-31').all()
    return issue

# Show a Specific Income by id
def issue_show(id: int, db: Session):
    issue = db.query(models.Issue).filter(models.Issue.id == id).first()
    if not issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The Issue with ID {id} is not found')
    return issue

# Create and Post a new Income
def issue_create(request: schemas.Issue, db: Session):
    print("CREATE ISSUE..............")
    new_issue = models.Issue(date=request.date, title = request.title, body = request.body, tags = request.tags, active = request.active, priority = request.priority, case_type = request.case_type, poject_id = request.poject_id, owner_id = request.owner_id)
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    print("CREATE ISSUE..............222222222")
    return new_issue

# Update an Issue
# def issue_update(id: int, request: schemas.Issue, db: Session):
#     query = text("""UPDATE income SET date=:date, service_income_1=:service_income_1, service_income_2=:service_income_2, bar_income_1=:bar_income_1, bar_income_2=:bar_income_2, pos=:pos, z_count=:z_count, vat=:vat, waitress_1=:waitress_1, waitress_2=:waitress_2, barman_1=:barman_1, barman_2=:barman_2, notes=:notes, shift_id=:shift_id WHERE id = :id""").params( date=request.date, service_income_1 = request.service_income_1, service_income_2 = request.service_income_2, bar_income_1=request.bar_income_1, bar_income_2=request.bar_income_2, pos=request.pos, z_count=request.z_count, vat=request.vat, waitress_1=request.waitress_1, waitress_2=request.waitress_2, barman_1=request.barman_1, barman_2=request.barman_2, notes=request.notes, shift_id=request.shift_id , id=id)
#     result = db.execute(query)
#     if not result:
#         raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail=f'The income with id {id} is not found')
#     db.commit()
#     return request

# Delete an Income
# def issue_destroy(id: int, db: Session):
#     income = db.query(models.Income).filter(models.Income.id == id)
#     if not income.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The income with id {id} is not found") 
#     income.delete(synchronize_session=False)
#     db.commit()
#     return "deleted!"



