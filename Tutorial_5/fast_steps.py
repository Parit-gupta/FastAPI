from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def root():
#     return "Hello World"

# INFO:  Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# This line shows the URL where your app is being served, in your local machine.
# FastAPI generates a "schema" with all your API using the OpenAPI standard for defining APIs.

"""
A schema is like a blueprint or a plan that describes how something is organized or structured. 
It tells you what parts something has and how they fit together, but it doesn’t show the actual details or 
the real thing itself.
"""

"""
API Schema
An API schema is like a detailed map or plan of your API. It shows:
What URLs (paths) your API has
What inputs (parameters) those URLs accept
What kind of data the API sends and receives
OpenAPI is a standard way to write this map so everyone understands your API the same way.

Data Schema
A data schema describes the structure or shape of the data itself — for example, a JSON object. It tells you:
What fields (attributes) are there
What types those fields are (number, string, boolean, etc.)

OpenAPI and JSON Schema Together
OpenAPI defines the overall API schema — the endpoints and how the API works.
Inside OpenAPI, the data schemas (using JSON Schema) describe what data looks like when sent or received.
"""

# @app.get("/items/{itemname}")
# async def item(itemname):
#     return {"message":f"this is your items name {itemname}"} # creating first api port


    