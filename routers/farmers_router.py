from fastapi import APIRouter,Depends
router = APIRouter()
from database.connection import get_db
from schemas.schema import Farmers
from services.farmer_services import *
from typing import List

@router.get("/Farmers",response_model=List[Farmers])
def get_farmers(db=Depends(get_db)):
    return get_farmer_service(db)

@router.get("/Farmers/{Id}",response_model=Farmers)
def get_farmer_by_id(Id : int,db = Depends(get_db)):
    return get_farmer_id_service(Id,db)

@router.post("/Farmers")
def create_farmer(farmer : Farmers,db = Depends(get_db)):
    return create_farmer_service(farmer,db)

@router.put("/Farmers/{Id}")

def update_farmer(Id : int, farmer : Farmers,db = Depends(get_db)):
    return update_farmer_service(Id, farmer,db)

@router.delete("/Farmers/{Id}")
def delete_farmer(Id : int,db = Depends(get_db)):
    return delete_farmer_service(Id,db)
    
