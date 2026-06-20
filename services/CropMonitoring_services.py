from datetime import datetime
from fastapi import HTTPException
from schemas.schema import CropMonitoring

def add_record_service(record: CropMonitoring,db):
    cursor = db.cursor(dictionary = True)
    cursor.execute(
        "INSERT INTO CropMonitoring (Id, FarmerCropID, MonitoringDate, PlantHeight, HealthStatus, Remarks, CapturedBy) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (
            record.Id,
            record.FarmerCropID,
            record.MonitoringDate,
            record.PlantHeight,
            record.HealthStatus,
            record.Remarks,
            record.CapturedBy,
        ),
    )
    if record.Id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Id must be a positive integer",
        )
    db.commit()
    return {"message": "Inserted Record Successfully"}

def get_history_service(FarmerCropId: int,db):
    cursor = db.cursor(dictionary = True)
    if FarmerCropId <= 0:
        raise HTTPException(
            status_code=400,
            detail="Id must be a positive integer",
        )

    cursor.execute(
        "SELECT * FROM CropMonitoring WHERE FarmerCropId = %s ORDER BY MonitoringDate DESC",
        (FarmerCropId,),
    )
    history = cursor.fetchall()

    if history is None:  
        raise HTTPException(
            status_code=404,
            detail=f"Crop monitoring history not found for FarmerCropId {FarmerCropId}",
        )

    return history

def update_record_service(Id: int, record: CropMonitoring,db):
    cursor = db.cursor(dictionary = True)
    cursor.execute(
        "UPDATE CropMonitoring SET FarmerCropID = %s, MonitoringDate = %s, PlantHeight = %s, HealthStatus = %s, Remarks = %s, CapturedBy = %s WHERE Id = %s",
        (
            record.FarmerCropID,
            record.MonitoringDate,
            record.PlantHeight,
            record.HealthStatus,
            record.Remarks,
            record.CapturedBy,
            Id,
        ),
    )
    db.commit()
    return {"message": "Updated Successfully"}

def get_records_service(FarmerCropId: int,db):
    cursor = db.cursor(dictionary = True)
    cursor.execute(
        "SELECT * FROM CropMonitoring WHERE FarmerCropID = %s",
        (FarmerCropId,),
    )
    return cursor.fetchall() 