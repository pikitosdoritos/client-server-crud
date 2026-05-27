from fastapi import FastAPI
from .endpoints import register, login
from backend.database import engine
from backend.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(register.router)
app.include_router(login.router)

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}