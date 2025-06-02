from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message":"Hello"}

# @app.get("/items/{item_name}")
# async def item(item_name):
#     return {"message":f"your selected item is {item_name}"}


# @app.get("/number/{number}")        # setting input as a integer parameter
# async def numb(number:int):
#     return {"message":number}

# @app.get("/file/{file_path:path}")
# async def file(file_path:str):
#     return {"path":file_path}      # path as a parameter

# @app.get("/{company}/product/{name}")       #multiple variables can be entered
# def name(company:str,name:str):
#     return {"company_name":company,"product_name":name}

# Query
import requests

res = requests.get("http://127.0.0.1:8000/items/?q=10")  # can see the context using the port and request with help of query writing 
print("Text",res.text)
print("JSON",res.json())
print("Status_Code",res.status_code)
