from sqlalchemy import Column,String,Integer
from database.sqlalchemy_db import Base

class CropMaster(Base):
    __tablename__= "CropsMaster"
    Id = Column(Integer,primary_key=True,index=True)
    CropName = Column(String((50)))
    Description = Column(String(100))
