from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List


class UserUpdate(BaseModel):
    email: EmailStr
    password: str
    new_email: EmailStr
    new_password: str


class UserNew(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(UserNew):
    ...


class TokenData(BaseModel):
    id: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class MemeData(BaseModel):
    url: str


class Meme(BaseModel):
    id: int
    url: str
    created_at: datetime

    class Config:
        orm_mode: True


class MemeOut(BaseModel):
    memes: List[Meme]

