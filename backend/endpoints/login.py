from fastapi import FastAPI, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from .. import models, schemas
from backend.security import verify_password

router = APIRouter(prefix="/login", tags=["login"])

@router.post("/user/login", response_model=schemas.LoginResponse)
def login_user(payload: schemas.LogIn, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == payload.email, 
    ).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    is_veryfied_password = verify_password(payload.password, user.password_hash)

    if not is_veryfied_password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    return {"message": "LogIn successful"}