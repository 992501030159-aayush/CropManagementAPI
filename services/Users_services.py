from schemas.schema import User as UserSchema,LoginUser
from fastapi import HTTPException
import bcrypt
from utils.logger import logger
from utils.jwt_handler import create_access_token
from models.user_model import Users as UserModel
from sqlalchemy.orm import Session

def login_user_service(user:LoginUser,db:Session):
    try:
        db_user = db.query(UserModel).filter(UserModel.Email == user.Email).first()
        if not db_user:
            raise HTTPException(
                status_code=401,
                detail="Invalid Email or Password!"
            )
        if not bcrypt.checkpw(
            user.Password.encode("utf-8"),
            db_user.Password.encode("utf-8")
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid Email or Password"
            )
        token = create_access_token(
            {
                "user_id": db_user.Id,
                "email": db_user.Email
            }
        )
        logger.info(f"Token created successfully for user {user.Email}")
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except HTTPException:
        raise
    except Exception:
        logger.exception("Couldn't create token")
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
def get_user_service(db):
    try:
        users = db.query(UserModel).all()
        logger.info("All users are displayed!")
        return users
    except Exception:
        logger.exception("Error while fetching the Users")
        raise

def get_user_by_id_service(Id : int,db : Session):
    try:
        if Id<=0:
            raise HTTPException(
                status_code=400,
                detail="Invalid Input"
            ) 
        data = db.query(UserModel).filter(UserModel.Id==Id).first()
        if not data:
            logger.warning(f"User with Id {Id} not found")
            raise HTTPException(
                status_code=404,
                detail="Record not found"
            )
        logger.info(f"User with Id {Id} was fetched successfully")
        return data
    except HTTPException:
        raise
    except Exception:
        logger.exception("Unexpected error occured")
        raise

def create_user_service(user: UserSchema, db):
    try:
        hashed_password = bcrypt.hashpw(
            user.Password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

        db_user = UserModel(
            Id=user.Id,
            Full_Name=user.Full_Name,
            Email=user.Email,
            Password=hashed_password,
            isActive=user.isActive
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info("Values inserted successfully")
        return {"message": "User has been created."}
    except Exception:
        db.rollback()
        logger.exception(f"Error while creating the user : {user.Email}")
        raise
def delete_user_service(Id : int,db):
    try:
        if (Id<=0):
            raise HTTPException(
                status_code=400,
                detail="Invalid Input"
            )
        user = db.query(UserModel).filter(UserModel.Id==Id).first()

        if not user:
            logger.warning(f"User with Id {Id} not found")
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        db.delete(user)
        db.commit()
        logger.info(f"User with Id {Id} was deleted")
        return {"message": "User Has been deleted"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception("could not delete User")
        raise