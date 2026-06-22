from fastapi import APIRouter,Depends
from database.sqlalchemy_db import get_db
from sqlalchemy.orm import Session
from schemas.schema import User,LoginUser
from services.Users_services import get_user_by_id_service,get_user_service,create_user_service,delete_user_service,login_user_service
from typing import List
router = APIRouter()
@router.post("/login")
def login_user(user : LoginUser,db:Session=Depends(get_db)):
    return login_user_service(user,db)

@router.get("/Users",response_model=List[User])
def get_users(db : Session= Depends(get_db)):
    return get_user_service(db)

@router.get("/Users/{Id}",response_model=User)
def get_user_by_id(Id : int,db : Session= Depends(get_db)):
    return get_user_by_id_service(Id,db)

@router.post("/Users")
def create_user(user : User,db : Session= Depends(get_db)):
    return create_user_service(user,db)

@router.delete("/Users/{Id}")
def delete_user(Id : int,db: Session= Depends(get_db)):
    return delete_user_service(Id,db) 
 

