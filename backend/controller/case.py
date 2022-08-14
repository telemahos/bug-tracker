from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..mvc import case, user, project
# from fastapi_pagination import pagination_params, Page, paginate
# from fastapi_pagination.limit_offset import pagination_params

router = APIRouter(
    prefix="/api/case",
    tags=['Case']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowCase]) 
async def all_case(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return case.case_get_all(db)

@router.get('/project/{project_id}', response_model = List[schemas.ShowCase], status_code=200)
async def show_case_by_project(project_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return case.case_show_by_project(project_id, db)

@router.get('/user/{owner_id}', response_model = List[schemas.ShowCase], status_code=200)
async def show_case_by_owner(owner_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return case.case_show_by_owner(owner_id, db)

@router.get('/case_type/{case_type}', response_model = List[schemas.ShowCase], status_code=200)
async def show_case_by_case_type(case_type: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return case.case_show_by_case_type(case_type, db)

@router.get('/priority/{priority}', response_model = List[schemas.ShowCase], status_code=200)
async def show_case_by_priority(priority: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return case.case_show_by_priority(priority, db)

@router.get('/active/{active}', response_model = List[schemas.ShowCase], status_code=200)
async def show_case_by_active(active: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return case.case_show_by_active(active, db)

@router.get('/{year}/{month}/', response_model = List[schemas.ShowCase], status_code=200)
async def show_case_by_date(year: str, month: str , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return case.case_show_by_date(year, month, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowCase)
async def show_case(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return case.case_show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_case(request: schemas.Case, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    print("CREATE CASE CONTROLLER..............")
    return case.case_create(request, db)

@router.delete('/{id}', status_code=status.HTTP_404_NOT_FOUND)
async def destroy_case(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return case.case_destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_case(id:int , request: schemas.Case, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return case.case_update(id, request, db) 

