from fastapi import APIRouter,Depends
router = APIRouter()
from database.sqlalchemy_db import get_db
from schemas.schema import FarmerCrops
from services.farmercrop_services import *
from typing import List
from sqlalchemy.orm import Session


@router.get("/FarmerCrops/{FarmerId}",response_model=List[FarmerCrops])
def get_FarmerCrops(FarmerId : int,db:Session= Depends(get_db)):
    return get_farmercrop_service(FarmerId,db)
@router.post("/FarmerCrops/{FarmerId}")
def assign_crop(FarmerId : int, crop : FarmerCrops,db:Session= Depends(get_db) ):
    return assigncrop_service(FarmerId,crop,db)
@router.put("/FarmerCrops/{Id}")
def update_status(Id : int, crop : FarmerCrops,db:Session= Depends(get_db)):
    return update_status_service(Id, crop,db)
@router.get("/FarmerCrops/history/{CropId}",response_model=List[FarmerCrops])
def crop_history(CropId : int,db:Session= Depends(get_db)):
    return crop_history_service(CropId,db)
