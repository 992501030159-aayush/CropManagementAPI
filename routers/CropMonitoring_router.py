from fastapi import APIRouter,Depends
router =  APIRouter()
from database.sqlalchemy_db import get_db
from schemas.schema import CropMonitoring
from services.CropMonitoring_services import *
from typing import List
from sqlalchemy.orm import Session
from utils.auth import get_current_user,require_role
@router.post("/CropMonitoring")
def add_record(record : CropMonitoring,db:Session= Depends(get_db),
               current_user = Depends(require_role(["admin","agriculture_officer"]))):
    return add_record_service(record,db)

@router.get("/CropMonitoring/{FarmerCropId}",response_model=List[CropMonitoring])
def get_history(FarmerCropId : int,db:Session= Depends(get_db),
                current_user = Depends(get_current_user)):
    return get_history_service(FarmerCropId,db)

@router.put("/CropMonitoring/{Id}")
def update_record(Id : int,record:CropMonitoring,db:Session= Depends(get_db),
                  current_user = Depends(require_role(["admin","agriculture_officer"]))):
    return update_record_service(Id,record,db)

@router.get("/CropMonitoring/by-farmer/{FarmerCropId}",response_model=List[CropMonitoring])
def get_records(FarmerCropId : int,db:Session= Depends(get_db),
                current_user = Depends(get_current_user)):
    return get_records_service(FarmerCropId,db)