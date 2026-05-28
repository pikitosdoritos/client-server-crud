from fastapi import FastAPI
from .endpoints import register, login
from backend.database import engine
from backend.models import Base
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


Base.metadata.create_all(bind=engine)

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

FRONTEND_DIR = BASE_DIR.parent / "frontend"

app.include_router(register.router)
app.include_router(login.router)

app.mount("/frontend", StaticFiles(directory=FRONTEND_DIR), name="frontend")

@app.get("/")
def read_index():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}