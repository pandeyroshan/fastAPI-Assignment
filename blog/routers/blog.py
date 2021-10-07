from sys import prefix
from blog.oauth2 import get_current_user
from fastapi import APIRouter, Depends, status, Response
from .. import schemas
from typing import List
from typing import List
from sqlalchemy.orm import Session
from .. import models
from blog import schemas
from ..database import get_db
from ..repository import blog
from ..oauth2 import get_current_user


router = APIRouter(
    prefix = '/blog',
    tags=["Blogs"]
)

@router.get("/", response_model = List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post("/", status_code=201)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)

@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    return blog.delete(id, db)

@router.put("/{id}", status_code = status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)

@router.get("/{id}", status_code = 200, response_model = schemas.ShowBlog)
def get_single_blog(id, response: Response,  db: Session = Depends(get_db)):
    return blog.get_single_post(id, response, db)