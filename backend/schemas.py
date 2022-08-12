from typing import List, Optional
from datetime import date
# datetime, time
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class NotesIn(BaseModel):
    date: Optional[date]
    title: Optional[str] = None
    body: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    author_id: Optional[int]

class NotesOut(BaseModel):
    id: Optional[int]
    date: Optional[date]
    title: Optional[str]
    body: Optional[str]
    tags:  Optional[str] 
    active:  Optional[bool]
    author_id: Optional[int]
    class Config():
        orm_mode = True

class BlogBase(BaseModel):
    id: Optional[int] = None
    date: Optional[date] 
    title: Optional[str] = None
    body: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    # author_id: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    user_role: int

class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    user_role: int
    # Refers to the first class Blog
    the_blogs: List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    id: int
    date: Optional[date] = None
    title: Optional[str] = None
    body: Optional[str] = None
    tags: Optional[str] = None
    active: Optional[bool] = False
    owner: ShowUser
    class Config():
        orm_mode = True

class login(BaseModel):
    username: str
    password: str


# Case
# ------------------------------------
class CaseBase(BaseModel):
    id: int
    date: date
    title: Optional[str] = None
    body: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    priority: Optional[int] = 0
    case_type: Optional[int] = 0
    poject_id: Optional[int] = None
    owner_id: Optional[int] = None

class Case(CaseBase):
    class Config():
        orm_mode = True

class ShowCase(CaseBase):
    id: int
    date: date
    title: Optional[str] = None
    body: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    priority: Optional[int] = 0
    case_type: Optional[int] = 0
    poject_id: Optional[int] = None
    owner_id: Optional[int] = None

    class Config():
        orm_mode = True

    # bar_income_2: Optional[float] = None
    # pos: float = 0
    # shift_id: Optional[str]
    # the_shift: Optional[Shift] 
    
# Project
# ------------------------------------
class ProjectBase(BaseModel):
    id: int
    date: date
    end_date : date
    title: Optional[str] = None
    description: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    priority: Optional[int] = 0
    team_id: Optional[int] = 0
    owner_id: Optional[int] = None

class Project(ProjectBase):
    class Config():
        orm_mode = True

class ShowProject(ProjectBase):
    id: int
    date: date
    end_date: date
    title: Optional[str] = None
    description: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    priority: Optional[int] = 0
    team_id: Optional[int] = 0
    owner_id: Optional[int] = None

    class Config():
        orm_mode = True