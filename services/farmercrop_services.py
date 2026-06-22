
from schemas.schema import FarmerCrops
from fastapi import HTTPException
from utils.logger import logger
from models.FarmerCrop import FarmerCrop as FC_Model
from sqlalchemy.orm import Session

def get_farmercrop_service(FarmerId : int,db:Session):
    try:
        if (FarmerId<=0):
            raise HTTPException(
                status_code=400,
                detail="invalid input"
            )
        db_user = db.query(FC_Model).filter(FC_Model.FarmerId==FarmerId).all()
        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="Record not found"
            )
        logger.info(f"FarmerCrops were fetched for farmerid {FarmerId}")
        return db_user
    except HTTPException:
        raise
    except Exception:
        logger.exception(f"Could not fetch farmercrop data for {FarmerId}")
        raise

def assigncrop_service(FarmerId: int,crop:FarmerCrops,db:Session):
    try:

        if (FarmerId<=0):
            raise HTTPException(
                status_code=400,
                detail="invalid input"
            )
        db_user = FC_Model(
            Id = crop.Id,
            FarmerId = crop.FarmerId,
            CropId = crop.CropId,
            AreaInAcres = crop.AreaInAcres,
            SowingDate = crop.SowingDate,
            ExpectedHarvestDate = crop.ExpectedHarvestDate,
            Status = crop.Status
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        logger.info(f"Assigned crop successfully to FarmerId {FarmerId}")
        return {"message" : "Crop assigned Successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception(f"Could not assign crop to farmer {FarmerId}")
        raise


def update_status_service(Id : int, crop : FarmerCrops,db:Session):
    try:
        if(Id<=0):
            raise HTTPException(
                status_code=400,
                detail="invalid input"
            )
        data = db.query(FC_Model).filter(FC_Model.Id==Id).first()
        if not data:
            raise HTTPException(
                status_code=404,
                detail="Record Not found"
            )
        data.AreaInAcres = crop.AreaInAcres
        data.SowingDate = crop.SowingDate
        data.ExpectedHarvestDate = crop.ExpectedHarvestDate
        data.Status = crop.Status
        db.commit()
        logger.info(f"Updated the farmercrop with id {Id}")
        return {"message" : "Status Updated Successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception(f"Could not update farmer crop for cropid {Id}")
        raise

def crop_history_service(CropId : int,db:Session):
    try:
        if CropId<=0:
            raise HTTPException(
                status_code=400,
                detail="Enter a valid CropId"
            )
        data = db.query(FC_Model).filter(FC_Model.CropId==CropId).all()
        logger.info(f"Crop history for cropid {CropId} fetched successfully")
        return data
    except HTTPException:
        raise
    except Exception:
        logger.exception(f"Could not fetch crop histoory for cropid {CropId}")
