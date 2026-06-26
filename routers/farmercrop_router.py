from fastapi import APIRouter,Depends
router = APIRouter()
from database.sqlalchemy_db import get_db
from schemas.schema import FarmerCrops
from services.farmercrop_services import *
from typing import List
from sqlalchemy.orm import Session
from utils.auth import get_current_user,require_role


@router.get("/FarmerCrops/{FarmerId}",response_model=List[FarmerCrops])
def get_FarmerCrops(FarmerId : int,
                    db:Session= Depends(get_db),
                    current_user = Depends(require_role(["admin","agriculture_officer"]))):
    return get_farmercrop_service(FarmerId,db)
@router.post("/FarmerCrops/{FarmerId}")
def assign_crop(FarmerId : int, crop : FarmerCrops,
                db:Session= Depends(get_db),
                current_user = Depends(require_role(["admin","agriculture_officer"]))):
    return assigncrop_service(FarmerId,crop,db)

@router.put("/FarmerCrops/{Id}")
def update_status(Id : int, crop : FarmerCrops,
                  db:Session= Depends(get_db),
                  current_user = Depends(require_role(["admin","agriculture_officer"]))):
    return update_status_service(Id, crop,db)

@router.get("/FarmerCrops/history/{CropId}",response_model=List[FarmerCrops])
def crop_history(CropId : int,db:Session= Depends(get_db),
                 current_user = Depends(require_role(["admin","agriculture_officer"]))):
    return crop_history_service(CropId,db)
