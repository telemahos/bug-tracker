from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
    user_role = Column(Integer) # admin=?, Dev=1, QA=2, BA=3, PM=4, TM=5

#---------------------------------------
class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True, index=True)
    case_nr = Column(String, index = True)
    start_date = Column(Date, index=True)
    due_date = Column(Date, index=True)
    title = Column(String, index = True)
    description = Column(String) 
    tags = Column(String)
    status = Column(Integer, default=0)
    priority = Column(Integer) # Low=1, Medium=2, High=3, Critical=4
    case_type = Column(Integer) # Issue=1, Bug=2, Note=3
    project_id = Column(Integer)
    owner_id = Column(Integer)

#---------------------------------------
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    project_nr = Column(String)
    start_date = Column(Date)
    due_date = Column(Date)
    title = Column(String, index = True)
    description = Column(String) 
    tags = Column(String)
    active = Column(Boolean, default=False)
    status = Column(Integer, default=0)
    priority = Column(Integer) # Low=0, Medium=1, High=2, Critical=3
    owner_id = Column(Integer)

    
#---------------------------------------
class TeamMember(Base):
    __tablename__ = 'team_members'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer)
    user_id = Column(Integer)
    team_role = Column(Integer)
    assign_date = Column(Date)
    active = Column(Boolean, default=False)
    note = Column(String)