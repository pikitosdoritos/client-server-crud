from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from .. import schemas, models
from hashlib import hash_password

router = APIRouter(prefix="/register", tags=["register"])

@router.post("/user/create", response_model=schemas.CreateUser)
def create_user(payload: schemas.CreateUser, db: Session = Depends(get_db)):

    user = models.User(
        name = payload.name,
        email = payload.email,
        password = payload.password,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user