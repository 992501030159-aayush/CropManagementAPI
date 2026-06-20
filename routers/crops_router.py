from fastapi import APIRouter,Depends   
from database.connection import get_db
from schemas.schema import CropsMaster
from services.cropsmaster_services import *
from typing import List
router = APIRouter()
@router.get("/CropsMaster",response_model=List[CropsMaster])
def get_crops(db= Depends(get_db)):
    return get_crops_services(db)

@router.get("/CropsMaster/{Id}",response_model=CropsMaster)
def get_crop_by_id(Id: int,db= Depends(get_db)):
    return get_crops_id_services(Id,db)

@router.post("/CropsMaster")
def create_crop(crop: CropsMaster,db= Depends(get_db)):
    return create_crop_service(crop,db)

@router.put("/CropsMaster/{Id}")
def update_crop(Id:int, crop:CropsMaster,db= Depends(get_db)):
    return update_crop_service(Id,crop,db)

@router.delete("/CropsMaster/{Id}")
def delete_crop(Id : int,db= Depends(get_db)):
    return delete_crop_service(Id,db)
