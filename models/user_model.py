from sqlalchemy import Column, Integer,String,Boolean
from database.sqlalchemy_db import Base
class Users(Base):
    __tablename__ = "Users" 
    Id = Column(Integer,primary_key=True,index=True)
    Full_Name = Column(String(50))
    Email = Column(String(50),unique=True)
    Password = Column(String(260))
    isActive = Column(Boolean,default=True)
