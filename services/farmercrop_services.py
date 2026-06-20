
from schemas.schema import FarmerCrops
from fastapi import HTTPException
from utils.logger import logger

def get_farmercrop_service(FarmerId : int,db):
    try:
        cursor = db.cursor(dictionary = True)
        if (FarmerId<=0):
            raise HTTPException(
                status_code=400,
                detail="invalid input"
            )
        cursor.execute("Select * from FarmerCrops where FarmerId = %s",(FarmerId,))
        data = cursor.fetchall()
        if not data:
            raise HTTPException(
                status_code=404,
                detail="Record not found"
            )
        logger.info(f"FarmerCrops were fetched for farmerid {FarmerId}")
        return data
    except HTTPException:
        raise
    except Exception:
        logger.exception(f"Could not fetch farmercrop data for {FarmerId}")
        raise

def assigncrop_service(FarmerId: int,crop:FarmerCrops,db):
    try:

        cursor = db.cursor()
        if (FarmerId<=0):
            raise HTTPException(
                status_code=400,
                detail="invalid input"
            )
        cursor.execute("Insert Into FarmerCrops(Id, FarmerId, CropId, AreaInAcres, SowingDate, ExpectedHarvestDate, Status) VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (crop.Id,FarmerId,crop.CropId,crop.AreaInAcres,crop.SowingDate,crop.ExpectedHarvestDate,crop.Status))
        
        if (crop.Id<=0):
            raise HTTPException(
                status_code=400,
                detail="invalid input"
            )
        db.commit()
        logger.info(f"Assigned crop successfully to FarmerId {FarmerId}")
        return {"message" : "Crop assigned Successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception(f"Could not assign crop to farmer {FarmerId}")
        raise


def update_status_service(CropId : int, crop : FarmerCrops,db):
    try:
        if(CropId<=0):
            raise HTTPException(
                status_code=400,
                detail="invalid input"
            )
        cursor = db.cursor(dictionary = True)

        cursor.execute(
            "Update FarmerCrops Set AreaInAcres = %s, SowingDate = %s, ExpectedHarvestDate = %s, Status = %s WHERE CropId = %s",
            (crop.AreaInAcres,crop.SowingDate,crop.ExpectedHarvestDate,crop.Status,CropId)
        )
        if(cursor.rowcount==0):
            raise HTTPException(
                status_code=404,
                detail="Record not found.."
            )
        db.commit()
        logger.info(f"Updated the farmercrop with id {CropId}")
        return {"message" : "Status Updated Successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception(f"Could not update farmer crop for cropid {CropId}")
        raise

def crop_history_service(CropId : int,db):
    try:
        if CropId<=0:
            raise HTTPException(
                status_code=400,
                detail="Enter a valid CropId"
            )
        cursor = db.cursor(dictionary = True)
        cursor.execute("Select * from FarmerCrops where CropId = %s",(CropId,))
        data = cursor.fetchall()
        logger.info(f"Crop history for cropid {CropId} fetched successfully")
        return data
    except HTTPException:
        raise
    except Exception:
        logger.exception(f"Could not fetch crop histoory for cropid {CropId}")
