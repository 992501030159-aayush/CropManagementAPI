# Crop Management API

## PROJECT OVERVIEW
A FastAPI- based Crop Management System for managing users,farmers,crops, and their monitoring.

## Techonology Stack
- Python
- FastAPI
- MySQL
- SQLALCHEMY
- JWT Authentication
- Bcrypt
- Uvicorn

# Installation Steps
```bash
pip install -r requirements.txt
```

## How to run application
```bash
uvicorn main:app --reload
```

## Swagger URL
http://127.0.0.1:8000/docs

## Folder Structure

```text
CropManagementAPI/
│.env
│   .gitignore
│   app.log
│   main.py
│   README.md
│   requirements.txt
│   
├───database
│   │   connection.py
│   │   sqlalchemy_db.py
│   
│ 
│           
├───models
│   │   CropMaster_model.py
│   │   cropmonitoring_model.py
│   │   CropTrackingHistory..py
│   │   FarmerCrop.py
│   │   Farmer_model.py
│   │   user_model.py
│   │   
│           
├───routers
│   │   CropMonitoring_router.py
│   │   crops_router.py
│   │   farmercrop_router.py
│   │   farmers_router.py
│   │   Users_router.py
│   
│   
├───schemas
│   │   schema.py
│   │   
│   └───__pycache__
│           schema.cpython-313.pyc
│           
├───services
│   │   CropMonitoring_services.py
│   │   cropsmaster_services.py
│   │   farmercrop_services.py
│   │   farmer_services.py
│   │   Users_services.py
│  
│           
├───utils
│   │   auth.py
│   │   jwt_handler.py
│   │   logger.py
│      
        

```


## Sample APIs
- POST/Users
- GET/Users
- GET/Users/{Id}
- POST/login
