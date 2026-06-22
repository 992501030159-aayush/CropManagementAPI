from schemas.schema import Farmers
from fastapi import HTTPException
from utils.logger import logger
from sqlalchemy.orm import Session
from models.Farmer_model import Farmer as farmer_model

def get_farmer_service(db:Session):
    try:
        data = db.query(farmer_model).all()
        logger.info(f"Fetched {len(data)} data successfully")
        return data
    except Exception:
        logger.exception("Error Displaying the farmers data!")
        raise
def get_farmer_id_service(Id : int,db:Session):
    try:
        if (Id<=0):
            raise HTTPException(
                status_code=400,
                detail="Invalid Id input"
            )
        
        data = db.query(farmer_model).filter(farmer_model.Id==Id).first()
        if not data:
            raise HTTPException(
                status_code=404,
                detail = "Record does not exist"
            )
        logger.info(f"Farmer with id {Id} was fetched successfully!")
        return data
    except HTTPException:
        raise
    except Exception:
        logger.exception(f"Could not fetch Farmer with id {Id}")
        raise

def create_farmer_service(farmer : Farmers,db:Session):
    try:
        db_user =  farmer_model(
            Id = farmer.Id,
            FarmerName = farmer.FarmerName,
            MobileNumber = farmer.MobileNumber,
            Address = farmer.Address,
            UserId = farmer.UserId
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"New farmer was inserted with Id {farmer.Id}")
        return {"message" : "Farmer inserted Successfully"}
    except Exception:
        db.rollback()
        logger.exception("Error while creating the farmer")
        raise

def delete_farmer_service(Id : int,db:Session):
    try:
        if (Id<=0):
            raise HTTPException(
                status_code=400,
                detail="Invalid Id input"
            )
        db_user = db.query(farmer_model).filter(farmer_model.Id==Id).first()
        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="Record not found"
        )
        db.delete(db_user)
        db.commit()
        logger.info(f"Farmer with id {Id} deleted successfully")
        return {"message":"Farmer deleted successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception(f"Error while deleting the Farmer with id {Id}")
        raise


def update_farmer_service(Id:int,farmer:Farmers,db:Session):
    try:
        if (Id<=0):
            raise HTTPException(
                status_code=400,
                detail="Invalid Id Input"
            )

        db_user = db.query(farmer_model).filter(farmer_model.Id==Id).first()
        if not db_user:
            logger.warning(f"FARMER with id {Id} not found for update")
            raise HTTPException(
                status_code=404,
                detail="Record not found"
            )
        db_user.FarmerName = farmer.FarmerName,
        db_user.MobileNumber = farmer.MobileNumber,
        db_user.Address = farmer.Address,
        db_user.UserId = farmer.UserId

        db.commit()
        logger.info(f"Farmer with Id {Id} was updated successfully!")
        return {"message" : "records updated successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception(f"Failed to update Farmer with id {Id}")
        raise


    