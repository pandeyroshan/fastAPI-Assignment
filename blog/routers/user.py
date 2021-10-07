from fastapi import APIRouter, Depends
from .. import schemas
from sqlalchemy.orm import Session
from blog import schemas
from ..database import get_db
from ..repository import users

router = APIRouter(
    prefix = '/user',
    tags=["Users"]
    )

@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return users.create(request, db)

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return users.get_user(id, db)