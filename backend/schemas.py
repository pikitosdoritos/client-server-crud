from pydantic import BaseModel


class OrmBase(BaseModel):
    model_config = {"from_attributes": True}

class CreateUser(BaseModel):
    name: str
    email: str
    password: str

class LogIn(BaseModel):
    email: str
    password: str