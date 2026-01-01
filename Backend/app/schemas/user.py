from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    email:str
    password:str

class LoginResponse(BaseModel):
    message:str
    user_id:int
    name:str

class LoginRequest(BaseModel):
    email: str
    password: str