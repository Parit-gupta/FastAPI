from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get():
    return "Hello world! How are you"

@app.get("/items")  # it is a query parameter as we are not writing q as a path parameter instead we are writing it in the code of displaying it
def item(q):
    return q

@app.get("/items")  
def item(q:int=0,skip:int=10):     # adding two query parameters to run on different python file
    return {"q":q,"skip":skip}

@app.get("/blogs")
def blogs(limit=10,published :bool=True):    # to rite default value we can do limit=10 but remember the number of variables you have to make all of them default if you try to makw single value default error will come
    if published:
        return f"{limit} blogs published"
    else:
        return f"{limit} blogs not published"
# to run this in the site only using link u should write "?limit=variable&published=true/false" as it is a query parameter