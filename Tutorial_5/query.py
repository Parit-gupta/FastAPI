from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get():
    return "Hello world! How are you"

@app.get("/items")  # it is a query parameter as we are not writing q as a path parameter instead we are writing it in the code of displaying it
def item(q):
    return q
