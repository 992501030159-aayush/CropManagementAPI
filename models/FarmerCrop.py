from sqlalchemy import Column,String,Date,Integer,ForeignKey,Float
# from sqlalchemy.orm import relationship
from database.sqlalchemy_db import Base

class FarmerCrop(Base):
    __tablename__ = "FarmerCrops"
    Id = Column(Integer,primary_key=True,index=True)
    FarmerId  = Column(Integer,ForeignKey("Farmers.Id"),nullable=False)
    CropId = Column(Integer,ForeignKey("CropsMaster.Id"),nullable=False)
    AreaInAcres = Column(Float)
    SowingDate = Column(Date)
    ExpectedHarvestDate = Column(Date)
    Status =  Column(String(20))

