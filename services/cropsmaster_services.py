from schemas.schema import CropsMaster
from fastapi import HTTPException
from utils.logger import logger

def get_crops_services(db):
    try:
        cursor = db.cursor(dictionary = True)
        cursor.execute("Select * FROM CropsMaster")
        data = cursor.fetchall()
        logger.info(f"Fetched {len(data)}  Crops successfully!")
        return data
    except Exception:
        logger.exception("Could not fetch Crops")
        raise

def get_crops_id_services(Id: int, db):
    try:
        if Id <= 0:
            raise HTTPException(
                status_code=400,
                detail="Value not valid"
            )

        cursor = db.cursor(dictionary=True)
        cursor.execute("Select * FROM CropsMaster where Id = %s", (Id,))
        data = cursor.fetchone()

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

def create_crop_service(crop : CropsMaster,db):
    try: 
        cursor = db.cursor()
        cursor.execute("Insert INTO CropsMaster(Id, CropName,Description) VALUES(%s,%s,%s)",(crop.Id,crop.CropName,crop.Description))
        db.commit()
        logger.info(f"Crop Created successfully with crop id {crop.Id}")
        return {"message" : "Values Inserted Successfully"}
    except Exception:
        db.rollback()
        logger.exception("Could not create the crop")
        raise

def update_crop_service(Id : int, crop:CropsMaster,db):
    cursor = db.cursor(dictionary = True)
    if Id<=0:
        raise HTTPException(
            status_code=400,
            detail="Value not valid"
        )
    cursor.execute(
        "Update CropsMaster Set CropName = %s, Description = %s where Id = %s",
        (crop.CropName, crop.Description, Id)
    )
    db.commit()
    return {"message":"Values updated successfully"}

def delete_crop_service(Id : int,db):
    try:
        cursor = db.cursor(dictionary = True)
        if Id<=0:
            raise HTTPException(
                status_code=400,
                detail="Value not valid"
            )
        cursor.execute("Delete From CropsMaster where Id = %s",(Id,))
        if cursor.rowcount==0:
            raise HTTPException(
                status_code=404,
                detail="Crop Not found"
            )
        db.commit()
        logger.info(f"Crop deleted successfully with id {Id}")
        return {"message" : "Crop Deleted Successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception("Could Not Delete the crop ")
        raise
