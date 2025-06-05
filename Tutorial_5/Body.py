"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

This example demonstrates how to handle multiple request bodies in a single endpoint. 
The endpoint receives an item_id as a path parameter, and two separate request bodies: one for Item and one 
for User. FastAPI automatically parses both into Pydantic models. The function returns a dictionary combining 
all inputs.
"""

"""
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
This example adds a third parameter importance that is passed in the request body, but is not part of a Pydantic model.
Using Annotated[int, Body()] lets you extract this field directly and independently from the rest of the model data.
"""


"""
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = Field(
        title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


Here, Field() is used to add metadata like title, description, and validation rules to model fields. The price field 
must be greater than 0. The request body is wrapped using Body(embed=True) so the payload is nested under a key (e.g.,
"item").
"""


"""
from typing import Annotated
from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/body")
def read(q:Annotated[str |None , Query(max_length=50)]):
    result = {"items": [{"author":"JK rowlings","title":"Harry potter"}]}
    if q:
        result.update({"q":q})
    return result

This example defines a GET endpoint that accepts an optional query parameter q. If provided, the response includes 
the query. The use of Annotated and Query() restricts the length of q to 50 characters.
"""


"""
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images

This POST endpoint accepts a JSON array of Image objects, each containing a validated HttpUrl and name. 
FastAPI parses the list automatically and returns it. This is useful for batch uploads or data collection.    

"""




"""
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str

img_list : List[Image] = []

@app.post("/image")
async def get_image(image:Image):
    img_list.append(image.url)       # reading in the list 
    return "Image urls have been uploaded"

@app.get("/image/geti")
async def retrive():
    return img_list


This example demonstrates simple in-memory storage of uploaded image URLs. When a POST request is made, 
the url from the image is added to a global list. A separate GET endpoint returns all stored URLs.    
"""



"""
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


In this version, Field(examples=[]) is used to provide example values that appear in the Swagger UI.
This helps developers understand the expected input format directly in the documentation.    
"""


# json example
"""
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results

    
This is an advanced example showing how to add multiple OpenAPI examples for a request body using 
Body(openapi_examples={...}). The examples are shown in Swagger UI, each with a summary and explanation. 
This is useful for educating users on correct vs incorrect input formats.

"""

"""
Some extra parameters

from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }
"""