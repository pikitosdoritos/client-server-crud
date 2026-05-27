from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from .. import schemas, models
from ..security import hash_password

router = APIRouter(prefix="/register", tags=["register"])

@router.post("/user/create", response_model=schemas.CreateUser)
def create_user(payload: schemas.CreateUser, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.email == payload.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="User with this email already exists")
    
    hashed_password = hash_password(payload.password)

    user = models.User(
        name = payload.name,
        email = payload.email,
        password = hashed_password,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user