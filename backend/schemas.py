from pydantic import BaseModel, EmailStr

class OrmBase(BaseModel):
    model_config = {"from_attributes": True}

class CreateUser(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserRead(OrmBase):
    id: int
    name: str
    email: EmailStr


class LogIn(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    message: str