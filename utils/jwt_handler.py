import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_access_token(data : dict):
    payload = data.copy()
    payload["exp"] = (datetime.utcnow() + timedelta(hours=1))
    token = jwt.encode(payload,
               SECRET_KEY,
               algorithm=ALGORITHM)
    return token
    