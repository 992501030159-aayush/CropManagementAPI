from schemas.schema import Farmers
from fastapi import HTTPException
from utils.logger import logger

def get_farmer_service(db):
    try:
        cursor = db.cursor(dictionary = True)
        cursor.execute("Select * FROM Farmers")
        data =  cursor.fetchall()
        logger.info(f"Fetched {len(data)} data successfully")
        return data
    except Exception:
        logger.exception("Error Displaying the farmers data!")
        raise
def get_farmer_id_service(Id : int,db):
    try:
        if (Id<=0):
            raise HTTPException(
                status_code=400,
                detail="Invalid Id input"
            )
        
        cursor = db.cursor(dictionary = True)
        cursor.execute("Select * FROM Farmers where Id = %s",(Id,))
        data = cursor.fetchone()
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

def create_farmer_service(farmer : Farmers,db):
    try:
        cursor = db.cursor(dictionary = True)
        cursor.execute(
            "INSERT INTO Farmers(Id, FarmerName, MobileNumber, Address, UserId) VALUES(%s,%s,%s,%s,%s)",
            (farmer.Id, farmer.FarmerName, farmer.MobileNumber, farmer.Address, farmer.UserId),
        )
        db.commit()
        logger.info(f"New farmer was inserted with Id {farmer.Id}")
        return {"message" : "Farmer inserted Successfully"}
    except Exception:
        db.rollback()
        logger.exception("Error while creating the farmer")
        raise

def delete_farmer_service(Id : int,db):
    try:
        if (Id<=0):
            raise HTTPException(
                status_code=400,
                detail="Invalid Id input"
            )
        cursor = db.cursor(dictionary = True)
        cursor.execute("DELETE From Farmers where Id = %s",(Id,))
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Record not found"
        )
        db.commit()
        logger.info(f"Farmer with id {Id} deleted successfully")
        return {"message":"Farmer deleted successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception(f"Error while deleting the Farmer with id {Id}")
        raise


def update_farmer_service(Id:int,farmer:Farmers,db):
    try:
        if (Id<=0):
            raise HTTPException(
                status_code=400,
                detail="Invalid Id Input"
            )
        cursor = db.cursor()
        cursor.execute(
            "Update Farmers SET FarmerName = %s, MobileNumber = %s, Address = %s, UserId = %s WHERE Id = %s",
            (farmer.FarmerName, farmer.MobileNumber, farmer.Address, farmer.UserId, Id),
        )
        if cursor.rowcount == 0:
            logger.warning(f"FARMER with id {Id} not found for update")
            raise HTTPException(
                status_code=404,
                detail="Record not found"
            )
        db.commit()
        logger.info(f"Farmer with Id {Id} was updated successfully!")
        return {"message" : "records updated successfully"}
    except HTTPException:
        raise
    except Exception:
        db.rollback()
        logger.exception(f"Failed to update Farmer with id {Id}")
        raise
    