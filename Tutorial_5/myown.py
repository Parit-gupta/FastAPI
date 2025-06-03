from typing import Annotated
from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/body")
def read(q:Annotated[str |None , Query(max_length=50)]):
    result = {"items": [{"author":"JK rowlings","title":"Harry potter"}]}
    if q:
        result.update({"q":q})
    return result
