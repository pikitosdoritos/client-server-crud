from fastapi import FastAPI, Depends, APIRouter, HTTPException
from .. import models, schemas
from sqlalchemy.orm import Session
from backend.database import get_db

router = APIRouter(prefix="/login", tags=["login"])

@router.post("/user/login", response_model=schemas.LogIn)
def login_user(payload: schemas.LogIn, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == payload.email, 
        models.User.password == payload.password,
    ).first()

    if user:
        return {"LogIn": "Succesful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid email or password")