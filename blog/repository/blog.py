from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from .. import models
from .. import schemas

def get_all(db: Session):
    return db.query(models.Blog).all()

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    
    blog.delete(synchronize_session=False)
    db.commit()
    
    return {"message" : f"Deleted blog {id}"}

def update(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    
    blog.update(request.dict())
    db.commit()

    return f'Updated Post with id {id}'

def get_single_post(id, response: Response,  db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} is not available")
    
    return blog