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
from requests_html import HTMLSession


router = APIRouter(
    tags=["Blogs"]
)

# Returns all the Blog
@router.get("/get_all_blog", response_model = List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

# Creates a blog
@router.post("/create_blog", status_code=201)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)

# Deletes a blog
@router.delete("/delete_blog/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    return blog.delete(id, db)

# Updates a Blog
@router.put("/update_blog/{id}", status_code = status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)

# Returns a Single Blog
@router.get("/get_blog/{id}", status_code = 200, response_model = schemas.ShowBlog)
def get_single_blog(id, response: Response,  db: Session = Depends(get_db)):
    return blog.get_single_post(id, response, db)

@router.get("/get_scrapy/{query}", status_code=200)
def get_scrapy(query):
    url = f"https://quotes.toscrape.com/tag/{query}"

    session = HTMLSession()
    response = session.get(url)

    qlist = []

    quotes = response.html.find("div.quote")

    for q in quotes:
        item = {
            'text' : q.find('span.text', first=True).text.strip(),
            'author' : q.find('small.author', first=True).text.strip(),
        }

        qlist.append(item)
    
    return qlist