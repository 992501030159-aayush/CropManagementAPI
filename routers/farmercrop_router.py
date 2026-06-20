from fastapi import APIRouter,Depends
router = APIRouter()
from database.connection import get_db
from schemas.schema import FarmerCrops
from services.farmercrop_services import *
from typing import List


@router.get("/FarmerCrops/{FarmerId}",response_model=List[FarmerCrops])
def get_FarmerCrops(FarmerId : int,db= Depends(get_db)):
    return get_farmercrop_service(FarmerId,db)
@router.post("/FarmerCrops/{FarmerId}")
def assign_crop(FarmerId : int, crop : FarmerCrops,db= Depends(get_db) ):
    return assigncrop_service(FarmerId,crop,db)
@router.put("/FarmerCrops/{CropId}")
def update_status(CropId : int, crop : FarmerCrops,db= Depends(get_db)):
    return update_status_service(CropId, crop,db)
@router.get("/FarmerCrops/history/{CropId}",response_model=List[FarmerCrops])
def crop_history(CropId : int,db= Depends(get_db)):
    return crop_history_service(CropId,db)
