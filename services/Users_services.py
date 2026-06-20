from schemas.schema import User,LoginUser
from fastapi import HTTPException
import bcrypt
from utils.logger import logger
from utils.jwt_handler import create_access_token


def login_user_service(login : LoginUser,db):
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("Select * From Users where Email = %s",(login.Email,))
        db_user = cursor.fetchone()
        if not db_user:
            raise HTTPException(
                status_code=401,
                detail="Invalid Email or Password"
            )
        if not bcrypt.checkpw(login.Password.encode('utf-8'),db_user["Password"].encode('utf-8')):
            raise HTTPException(
                status_code=401,
                detail="Invalid Email or Password"
            )
        token  = create_access_token({"sub" : str(db_user["Id"]),
                                     "Email" : str(db_user["Email"])})
        logger.info("Token Created Successfully %s",token)
        return {"access_token" : token,
                "type" : "bearer"}

    except HTTPException:
        raise
    except Exception:
        logger.exception("Could not create access token")
        raise
    finally:
        cursor.close()
        
def get_user_service(db):
    try:
        cursor = db.cursor(dictionary = True)
        cursor.execute("Select * from Users")
        logger.info("All users are displayed!")
        return cursor.fetchall()
    except Exception:
        logger.exception("Error while fetching the Users")
        raise

def get_user_by_id_service(Id : int,db):
    try:
        if Id<=0:
            raise HTTPException(
                status_code=400,
                detail="Invalid Input"
            ) 
        cursor = db.cursor(dictionary = True)
        cursor.execute("Select * from Users where Id = %s",(Id,))
        data = cursor.fetchone()
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

def create_user_service(user : User,db):
    try:
        cursor = db.cursor(dictionary = True)
        hashed_password = bcrypt.hashpw(
            user.Password.encode('utf-8'),
            bcrypt.gensalt()).decode('utf-8')
        
        cursor.execute("INSERT INTO Users(Id,Full_Name,Email,Password,isActive) VALUES(%s,%s,%s,%s,%s)",(user.Id,user.Full_Name,user.Email,hashed_password,user.isActive))
        db.commit()
        logger.info("Values inserted successfully")
        return {"messsage":"User has been created."}
    except Exception:
        db.rollback()
        logger.exception(f"Error while creating the user : {user.Email}")
        raise
def delete_user_service(Id : int,db):
    try:
        cursor = db.cursor(dictionary = True)
        if (Id<=0):
            raise HTTPException(
                status_code=400,
                detail="Invalid Input"
            )
        cursor.execute("SELECT * FROM Users WHERE Id = %s", (Id,))
        user = cursor.fetchone()

        if not user:
            logger.warning(f"User with Id {Id} not found")
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        cursor.execute("Delete From Users where Id = %s",(Id,))
        db.commit()
        logger.info(f"User with Id {Id} was deleted")
        return {"message": "User Has been deleted"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception("could not delete User")
        raise