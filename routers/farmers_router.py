from fastapi import APIRouter,Depends
router = APIRouter()
from database.sqlalchemy_db import get_db
from schemas.schema import Farmers
from services.farmer_services import *
from typing import List
from sqlalchemy.orm import Session
from utils.auth import get_current_user,require_role

@router.get("/Farmers",response_model=List[Farmers])
def get_farmers(db:Session=Depends(get_db),
                current_user = Depends(get_current_user)):
    return get_farmer_service(db)

@router.get("/Farmers/{Id}",response_model=Farmers)
def get_farmer_by_id(Id : int,
                     db:Session = Depends(get_db),
                     current_user = Depends(get_current_user)):
    return get_farmer_id_service(Id,db)

@router.post("/Farmers")
def create_farmer(farmer : Farmers,db:Session = Depends(get_db),
                  curret_user = Depends(require_role(["admin","agriculture_officer"]))):
    return create_farmer_service(farmer,db)

@router.put("/Farmers/{Id}")

def update_farmer(Id : int, farmer : Farmers,
                  db:Session = Depends(get_db),
                  curret_user = Depends(require_role(["admin","agriculture_officer"]))):
    return update_farmer_service(Id, farmer,db)

@router.delete("/Farmers/{Id}")
def delete_farmer(Id : int,db:Session = Depends(get_db),
                  curret_user = Depends(require_role("admin"))):
    return delete_farmer_service(Id,db)
    
