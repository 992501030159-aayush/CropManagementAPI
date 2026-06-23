from datetime import datetime
from fastapi import HTTPException
from schemas.schema import CropMonitoring
from sqlalchemy.orm import Session
from models.cropmonitoring_model import CropMonitoring as CMG_Model
from utils.logger import logger

def add_record_service(record: CropMonitoring,db:Session):
    try:
        db_user = CMG_Model(
            Id = record.Id,
            FarmerCropId = record.FarmerCropID,
            MonitoringData = record.MonitoringDate,
            PlantHeight = record.PlantHeight,
            HealthStatus = record.HealthStatus,
            Remarks = record.Remarks,
            CapturedBy = record.CapturedBy
        )
        if record.Id <= 0:
            raise HTTPException(
                status_code=400,
                detail="Id must be a positive integer",
            )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"Record Inserted successfully with Id = {record.Id}")
        return {"message": "Inserted Record Successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception("Could not add record!")
        raise

def get_history_service(FarmerCropId: int,db:Session):
    try:
        if FarmerCropId <= 0:
            raise HTTPException(
                status_code=400,
                detail="Id must be a positive integer",
            )

        history = db.query(CMG_Model).filter(CMG_Model.FarmerCropId==FarmerCropId).order_by(CMG_Model.MonitoringDate.desc()).all()

        if history is None:  
            raise HTTPException(
                status_code=404,
                detail=f"Crop monitoring history not found for FarmerCropId {FarmerCropId}",
            )
        logger.info(f"Fetched the history Of all crops with FarmerCropId {FarmerCropId}")
        return history
    except HTTPException:
        raise
    except Exception:
        logger.exception(f"Could not fetch history for Crops with FarmerCropId = {FarmerCropId}")
        raise
    
def update_record_service(Id: int, record: CropMonitoring,db:Session):
    try:
        if Id<=0:
            raise HTTPException(
                status_code=400,
                detail="Enter a valid Id"
            )
        data = db.query(CMG_Model).filter(CMG_Model.Id==Id).first()
        if not data:
            raise HTTPException(
                status_code=404,
                detail="Record Not found!"
            )
        data.MonitoringDate = record.MonitoringDate
        data.PlantHeight = record.PlantHeight
        data.HealthStatus = record.HealthStatus
        data.Remarks = record.Remarks
        data.CapturedBy = record.CapturedBy
        db.commit()
        logger.info(f"Updated records successfully with Id = {Id}")
        return {"message": "Updated Successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception(f"Could not update the record with Id {Id}")
        raise

def get_records_service(FarmerCropId: int,db:Session):
    try:
        if FarmerCropId<=0:
            raise HTTPException(
                status_code=400,
                detail="Enter a valid FarmerCropId"
            )
        data = db.query(CMG_Model).filter(CMG_Model.FarmerCropId==FarmerCropId).all()
        logger.info(f"Successfully fetched the records with FarmerCropId {FarmerCropId}")
        return data
    except HTTPException:
        raise
    except Exception:
        logger.exception(f"Could not get records for crop with FarmerCropId {FarmerCropId}")
        raise
