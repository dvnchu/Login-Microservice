from typing import Union
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserLogin(BaseModel):
   login_identifier: Union[EmailStr, str]
   password: str