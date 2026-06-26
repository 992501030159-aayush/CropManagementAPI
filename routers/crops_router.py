from fastapi import APIRouter,Depends   
from database.sqlalchemy_db import get_db
from schemas.schema import CropsMaster
from services.cropsmaster_services import *
from typing import List
from sqlalchemy.orm import Session
from utils.auth import get_current_user,require_role
router = APIRouter()
@router.get("/CropsMaster",response_model=List[CropsMaster])
def get_crops(db:Session= Depends(get_db),
             current_user = Depends(get_current_user)):
    return get_crops_services(db)

@router.get("/CropsMaster/{Id}",response_model=CropsMaster)
def get_crop_by_id(Id: int,db:Session= Depends(get_db),
                   current_user = Depends(get_current_user)):
    return get_crops_id_services(Id,db)

@router.post("/CropsMaster")
def create_crop(crop: CropsMaster,db:Session= Depends(get_db),
                current_user = Depends(require_role(["admin","agriculture_officer"]))):
    return create_crop_service(crop,db)

@router.put("/CropsMaster/{Id}")
def update_crop(Id:int, crop:CropsMaster,db:Session= Depends(get_db),
                current_user = Depends(require_role(["admin","agriculture_officer"]))):
    return update_crop_service(Id,crop,db)

@router.delete("/CropsMaster/{Id}")
def delete_crop(Id : int,db:Session= Depends(get_db),
                current_user = Depends(require_role("admin"))):
    return delete_crop_service(Id,db)
