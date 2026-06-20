from sqlalchemy import Column,ForeignKey,Integer,String,Date
from database.sqlalchemy_db import Base

class CropTrackingHistory(Base):
    __tablename__ = "CropTrackingHistory"
    Id = Column(Integer,primary_key=True,index = False)
    FarmerCropId = Column(Integer,ForeignKey("FarmerCrops.Id"),nullable=False)
    Status = Column(String(20))
    Remarks = Column(String(20))
    UpdatedOn = Column(Date)
    UpdatedBy = Column(String(50))