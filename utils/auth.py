from jose import jwt,JWTError
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from utils.jwt_handler import verify_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)
def get_current_user(token:str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is  None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    return payload

def require_role(role:str):
    def role_checker(current_user = Depends(get_current_user)):
        if current_user["Role"] != role:
            raise HTTPException(
                status_code=403,
                detail="Access Denied"
            )
        return current_user
    return role_checker



