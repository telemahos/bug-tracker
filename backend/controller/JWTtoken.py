from typing import Optional
from datetime import datetime, timedelta
from fastapi import Depends
from jose import JWTError, jwt
from .. import schemas


# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=jwt#about-jwt
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "d94183b53dc8fb24a48a9b3ea932509627a673081d85c072f4c9b5fec3816402"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 300


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception