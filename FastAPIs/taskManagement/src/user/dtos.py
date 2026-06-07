from pydantic import BaseModel
from typing import Optional

class UserRequest(BaseModel):
    name : str
    username : str
    password :str
    email :str
    phone_number : Optional[str] = None


class UserResponse(BaseModel):
    id : int
    name : str
    username : str
    email : str
    phone_number : Optional[str] = None

class LoginSchema(BaseModel):
    username: str
    password: str  
