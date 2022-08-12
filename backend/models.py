from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from .database import Base

class Notes(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    title = Column(String, index = True)
    body = Column(String, index = True) 
    tags = Column(String, index = True)
    active = Column(Boolean, default=False)
    author_id = Column(Integer,ForeignKey("users.id"))

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    title = Column(String, index = True)
    body = Column(String, index = True) 
    tags = Column(String, index = True)
    active = Column(Boolean, default=False)
    author_id = Column(Integer,ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="the_blogs")
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
    user_role = Column(Integer) # admin=?, Dev=1, QA=2, BA=3, PM=4, TM=5
    the_blogs = relationship("Blog", back_populates="owner")



#---------------------------------------
class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    title = Column(String, index = True)
    body = Column(String) 
    tags = Column(String)
    active = Column(Boolean, default=False)
    priority = Column(Integer) # Low=0, Medium=1, High=2, Critical=3
    case_type = Column(Integer) # Issue=0, Bug=1
    poject_id = Column(Integer)
    owner_id = Column(Integer,ForeignKey("users.id"))

    # shift_id = Column( String, ForeignKey('shift.id'), nullable=False)
    # the_shift = relationship("Shift", back_populates="the_income")
    # insurance = Column(Float)
    # outcome_id = Column(Integer, ForeignKey("outcome.id"), index=True, nullable=False)

#---------------------------------------
class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    end_date = Column(Date)
    title = Column(String, index = True)
    description = Column(String) 
    tags = Column(String)
    active = Column(Boolean, default=False)
    priority = Column(Integer) # Low=0, Medium=1, High=2, Critical=3
    team_id = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

#---------------------------------------
class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("project.id"))
    team_role = Column(Integer)
    assign_date = Column(Date)
    active = Column(Boolean, default=False)
    note = Column(String)