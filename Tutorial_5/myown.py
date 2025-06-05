from typing import Annotated
from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/body")
# def read(q:Annotated[str |None , Query(max_length=50)]=None):       # with annotation
def read(q:str = Query(default="Hundered",max_length=50)):
    result = {"items": [{"author":"JK rowlings"},{"title":"Harry potter"}]}
    if q:
        result["q"]=q
    return result
