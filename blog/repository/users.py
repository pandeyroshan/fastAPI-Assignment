from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from .. import models
from .. import schemas
from .. import hashing

def create(request: schemas.User, db: Session):
    hashed_password = hashing.hash(request.password)
    new_user = models.User(username=request.username, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user found with id {id}")
    return user