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
  
    # the_project = relationship("Project", back_populates="project_owner")
    # the_case = relationship("Case", back_populates="case_owner")
    # the_team_member = relationship("Team_Member", back_populates="team_member")

#---------------------------------------
class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    title = Column(String, index = True)
    description = Column(String) 
    tags = Column(String)
    status = Column(Integer, default=0)
    priority = Column(Integer) # Low=0, Medium=1, High=2, Critical=3
    case_type = Column(Integer) # Issue=0, Bug=1
    project_id = Column(Integer)
    owner_id = Column(Integer)
    # owner_id = Column(Integer,ForeignKey("users.id"))

    # case_owner = relationship("User", back_populates="the_case")
    # shift_id = Column( String, ForeignKey('shift.id'), nullable=False)
    # the_shift = relationship("Shift", back_populates="the_income")
    # insurance = Column(Float)
    # outcome_id = Column(Integer, ForeignKey("outcome.id"), index=True, nullable=False)

#---------------------------------------
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    end_date = Column(Date)
    title = Column(String, index = True)
    description = Column(String) 
    tags = Column(String)
    active = Column(Boolean, default=False)
    priority = Column(Integer) # Low=0, Medium=1, High=2, Critical=3
    team_id = Column(Integer)
    owner_id = Column(Integer)
    
    # project_owner = relationship("User", back_populates="the_project")
    # the_team = relationship("Team", back_populates="the_project_team")

#---------------------------------------
class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(String, ForeignKey("projects.id"))
    active = Column(Boolean, default=False)
    note = Column(String)
    
    the_members = relationship("TeamMember", back_populates="the_team")
    # the_project_team = relationship("Project", back_populates="the_team")
    
#---------------------------------------
class TeamMember(Base):
    __tablename__ = 'team_members'
    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    user_id = Column(Integer)
    team_role = Column(Integer)
    assign_date = Column(Date)
    active = Column(Boolean, default=False)
    note = Column(String)
    
    the_team = relationship("Team", back_populates="the_members")
    # team_member = relationship("User", back_populates="the_team_member")