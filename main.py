from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data' : f'{limit} blogs from the published list'}
    return {'data' : f'{limit} blogs from the list'}

@app.post('/blog')
def create_blog(blog: Blog):
    return {"data" : f"Blog is created with {blog}"}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)