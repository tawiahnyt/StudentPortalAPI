import os
import jwt
from pathlib import Path
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session
from dotenv import load_dotenv

from db.database import get_db
from db.schemas import TokenData
from db.models.student_data import StudentData

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


SECRET_KEY = '42b4c8bede484a5ee6ab804f52cdf50db4e7bdbd3fa4f813c19dfe3aaaf025f1'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

router = APIRouter()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, student_id: int):
    db_user = db.query(StudentData).filter(StudentData.student_id == student_id).first()
    return db_user


def authenticate_user(db: Session, student_id: int, password: str):
    user = get_user(db, student_id)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        student_id: int = payload.get("sub")
        if student_id is None:
            raise credentials_exception
        token_data = TokenData(student_id=student_id)
    except InvalidTokenError:
        raise credentials_exception

    user = db.query(StudentData).filter(StudentData.student_id == token_data.student_id).first()
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: StudentData = Depends(get_current_user)):
    return current_user
