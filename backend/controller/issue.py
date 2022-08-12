from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..mvc import user, issue
# from fastapi_pagination import pagination_params, Page, paginate
# from fastapi_pagination.limit_offset import pagination_params

router = APIRouter(
    prefix="/api/issue",
    tags=['issue']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowIssue]) 
# @router.get('/', response_model=Page[schemas.ShowIssue], dependencies=[Depends(pagination_params)])
async def all_issue(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # return paginate(issue.get_all(db))
    return issue.issue_get_all(db)

# @router.get('/{year}/{month}/', response_model=Page[schemas.ShowIssue], status_code=200, dependencies=[Depends(pagination_params)])
@router.get('/{year}/{month}/', response_model = List[schemas.ShowIssue], status_code=200)
async def show_issue_by_date(year: str, month: str , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # return paginate(issue.show_by_date(year, month, db))
    return issue.issue_show_by_date(year, month, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowIssue)
async def show_issue(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return issue.issue_show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_issue(request: schemas.Issue, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    print("CREATE ISSUE CONTROLLER..............")
    return issue.issue_create(request, db)

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_issue(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return issue.issue_destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_issue(id:int , request: schemas.Issue, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return issue.issue_update(id, request, db) 

