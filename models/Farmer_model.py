from sqlalchemy import Column,Integer,String,ForeignKey
from database.sqlalchemy_db import Base
from sqlalchemy.orm import relationship
class Farmer(Base):
    __tablename__ = "Farmers"
    Id = Column(Integer,primary_key=True,index=True)
    FarmerName = Column(String(50))
    MobileNumber = Column(String(10),unique=True)
    Address = Column(String(100))
    UserId = Column(Integer,ForeignKey = ("Users.Id"),nullable=False)