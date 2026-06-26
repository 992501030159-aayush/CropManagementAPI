from datetime import datetime, timedelta
from jose import jwt,JWTError
from fastapi import HTTPException
import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_access_token(data : dict):
    payload = data.copy()
    payload["exp"] = (datetime.utcnow() + timedelta(hours= 1))
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm = ALGORITHM
    )
    return token
def verify_token(token:str):
    try:
        payload  = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )