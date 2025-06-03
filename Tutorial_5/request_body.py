from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# @app.post("/blogs")         # you can see it in the fastapi document section but cannot directly run on browser 
# async def blogs():
#     return {"message":"how are your blogs"}


"""
Difference between post and get methods
| Feature                   | GET                                      | POST                                              
| ------------------------- | -----------------------------------      | -------------------------------------------------
| Purpose                   | Retrieve **data**                        |Send/submit **data** (e.g., form, JSON)            
| Browser-friendly          | Yes – works by typing URL                |No – browser doesn’t support directly typing POST 
| Where is data sent?       | In the **URL** (query string)            |In the **body** of the request                   
| Security                  | Less secure (data visible in URL)        |More secure (data hidden in body)                
| Data limit                | Limited (\~2KB, varies by browser)       |Large payload supported (files, forms)           
| Idempotent?               | Yes – Same request = same result         |No – Can change state (create new data)          
| Used for?                 | Reading/viewing data                     |Submitting data: forms, logins, uploads          

"""

class Blog(BaseModel):
    title:str
    name:str
    number:int

@app.post("/blogs")
def blog(blog:Blog):
    return f"blog is created and the blog name is {blog.title}"

"""
In this FastAPI application, we define an endpoint to create a blog using a POST request. First, the Blog class inherits from BaseModel, 
which is part of Pydantic — a powerful library that FastAPI uses for data validation. This class defines the structure of the expected 
input with three fields: title (a string), name (a string), and number (an integer). When a client sends a POST request to the /blogs 
endpoint with a JSON body, FastAPI automatically validates that the input matches the Blog model. If the input is correct, the function 
blog(blog: Blog) is called, where the parsed input is available as a blog object. The function then returns a message including the blog title.
This setup ensures clean, type-safe handling of request data, and FastAPI takes care of error handling, input parsing, and documentation 
generation automatically.
"""

# A cool small working project till I have learned

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