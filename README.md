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
│
├── database/
│   └── connection.py
│
├── models/
│
├── routers/
│   ├── CropMonitoring_router.py
│   ├── crops_router.py
│   ├── farmercrop_router.py
│   ├── farmers_router.py
│   └── Users_router.py
│
├── schemas/
│   └── schema.py
│
├── services/
│   ├── CropMonitoring_services.py
│   ├── cropsmaster_services.py
│   ├── farmercrop_services.py
│   ├── farmer_services.py
│   └── Users_services.py
│
├── utils/
│   ├── jwt_handler.py
│   └── logger.py
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```


## Sample APIs
- POST/Users
- GET/Users
- GET/Users/{Id}
- POST/login
