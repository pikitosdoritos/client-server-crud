from fastapi import FastAPI, Depends, APIRouter
from .. import models, schemas

router = APIRouter(prefix="login", tags=["login"])

@router.post("/user/login", response_model=)