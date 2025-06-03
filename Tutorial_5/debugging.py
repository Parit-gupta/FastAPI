from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title : str
    author : str
    price : int

blog_list : List[Blog]= []

@app.post("/blogs")
def blogs(blog:Blog):
    blog_list.append(blog)
    return f"blog is added successfully and the title is {blog.title}"

@app.get("/blogs")
def list():
    return {"list":blog_list}

@app.get("/blogs/total")
def total():
    sum=0
    for i in blog_list:
        sum = sum + i.price
    return{"total amount is":sum}