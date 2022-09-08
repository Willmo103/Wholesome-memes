from pydantic import BaseModel, EmailStr
from datetime import datetime


# class User(BaseModel):
#     id: int
#     email: EmailStr
#     password: str
#     created_at: datetime
#

class UserNew(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True
