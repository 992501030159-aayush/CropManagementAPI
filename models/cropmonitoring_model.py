from sqlalchemy import Column,Integer,String,Float,ForeignKey,Date
from database.sqlalchemy_db import Base

class CropMonitoring(Base):
    __tablename__ = "CropMonitoring"
    Id = Column(Integer,primary_key=True,index=True)
    FarmerCropId = Column(Integer,ForeignKey("FarmerCrops.Id"),nullable=False)
    MonitoringDate = Column(Date)
    PlantHeight = Column(Float)
    HealthStatus = Column(String(20))
    Remarks = Column(String(20))
    CapturedBy = Column(String(50))