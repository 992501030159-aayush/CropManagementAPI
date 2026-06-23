from fastapi import FastAPI
import uvicorn
from routers.Users_router import router as user_router
from routers.farmers_router import router as farmer_router
from routers.farmercrop_router import router as farmercrop_router
from routers.crops_router import router as cropmaster_router
from routers.CropMonitoring_router import router as cropmonitor_router

from models import *
from database.sqlalchemy_db import Base,engine
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(
    user_router,
    tags=["Users"]
)

app.include_router(
    farmer_router,
    tags=["Farmers"]
)

app.include_router(
    farmercrop_router,
    tags=["FarmerCrop"]
)

app.include_router(
    cropmaster_router,
    tags = ["CropMaster"]
)
app.include_router(
    cropmonitor_router,
    tags = ["Crop_Monitoring"]
)
if __name__ == ("__main__"):
    uvicorn.run(app, host="localhost", port=8000)
