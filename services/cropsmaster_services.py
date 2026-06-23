from schemas.schema import CropsMaster
from fastapi import HTTPException
from utils.logger import logger
from sqlalchemy.orm import Session
from models.CropMaster_model import CropsMaster as CM_Model

def get_crops_services(db:Session):
    try:
        data = db.query(CM_Model).all() 
        logger.info(f"Fetched {len(data)}  Crops successfully!")
        return data
    except Exception:
        logger.exception("Could not fetch Crops")
        raise

def get_crops_id_services(Id: int, db:Session):
    try:
        if Id <= 0:
            raise HTTPException(
                status_code=400,
                detail="Value not valid"
            )

        data = db.query(CM_Model).filter(CM_Model.Id == Id).first()

        if not data:
            raise HTTPException(
                status_code=404,
                detail="Record Not found"
            )
        logger.info(f"Fetched Crop with Id {Id}")
        return data

    except HTTPException:
        raise

    except Exception:
        logger.exception("Could not fetch Crop by Id")
        raise

def create_crop_service(crop : CropsMaster,db:Session):
    try: 
        db_user = CM_Model(
            Id = crop.Id,
            CropName = crop.CropName,
            Description = crop.Description
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"Crop Created successfully with crop id {crop.Id}")
        return {"message" : "Values Inserted Successfully"}
    except Exception:
        db.rollback()
        logger.exception("Could not create the crop")
        raise

def update_crop_service(Id : int, crop:CropsMaster,db:Session):
    if Id<=0:
        raise HTTPException(
            status_code=400,
            detail="Value not valid"
        )
    data = db.query(CM_Model).filter(CM_Model.Id==Id).first()
    if not data:
        raise HTTPException(
            status_code=404,
            detail="Record Not found!"
        )
    data.CropName = crop.CropName
    data.Description = crop.Description
    db.commit()
    return {"message":"Values updated successfully"}

def delete_crop_service(Id : int,db:Session):
    try:
        if Id<=0:
            raise HTTPException(
                status_code=400,
                detail="Value not valid"
            )
        data = db.query(CM_Model).filter(CM_Model.Id==Id).first()
        if not data:
            raise HTTPException(
                status_code=404,
                detail="Record Not found"
            )
        db.delete(data)
        db.commit()
        logger.info(f"Crop deleted successfully with id {Id}")
        return {"message" : "Crop Deleted Successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception("Could Not Delete the crop ")
        raise
