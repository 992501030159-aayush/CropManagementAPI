from pydantic import BaseModel
from datetime import date
class User(BaseModel):
    Id : int
    Full_Name : str
    Email : str
    Password : str
    isActive : bool

class Farmers(BaseModel):
    Id : int
    FarmerName : str
    MobileNumber : str
    Address : str
    UserId : int
class CropsMaster(BaseModel):
    Id : int
    CropName : str
    Description : str
class FarmerCrops(BaseModel):
    Id : int
    FarmerId : int
    CropId : int
    AreaInAcres : float
    SowingDate : date
    ExpectedHarvestDate : date
    Status : str
class CropMonitoring(BaseModel):
    Id : int
    FarmerCropID : int
    MonitoringDate : date
    PlantHeight : float
    HealthStatus : str
    Remarks : str
    CapturedBy : str
class CropTrackingHistory(BaseModel):
    Id : int
    FarmerCropID : int
    Status : str
    Remarks : str
    UpdatedOn : date
    UpdatedBy : str
class LoginUser(BaseModel):
    Email : str 
    Password : str
    