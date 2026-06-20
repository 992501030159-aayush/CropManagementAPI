from fastapi import APIRouter,Depends
router =  APIRouter()
from database.connection import get_db
from schemas.schema import CropMonitoring
from services.CropMonitoring_services import *
from typing import List
@router.post("/CropMonitoring")
def add_record(record : CropMonitoring,db= Depends(get_db)):
    return add_record_service(record,db)

@router.get("/CropMonitoring/{FarmerCropId}",response_model=List[CropMonitoring])
def get_history(FarmerCropId : int,db= Depends(get_db)):
    return get_history_service(FarmerCropId,db)

@router.put("/CropMonitoring/{Id}")
def update_record(Id : int,record:CropMonitoring,db= Depends(get_db)):
    return update_record_service(Id,record,db)

@router.get("/CropMonitoring/by-farmer/{FarmerCropId}",response_model=List[CropMonitoring])
def get_records(FarmerCropId : int,db= Depends(get_db)):
    return get_records_service(FarmerCropId,db)