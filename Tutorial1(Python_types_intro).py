"""
Python lets you add types to your code. These are called type hints.
Type hints show what kind of data a variable should have (like a number, text, etc.).
They help your code editor give you suggestions and find mistakes.
FastAPI uses type hints a lot. They make FastAPI faster, smarter, and easier to use.
"""

# Code 1

def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))

# now if we want to add types to this so that we can get recommendations for title we can do 
def get_full_name(first_name : str, last_name : str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))

# here we use : not isequalto 

# You can also get error checks 
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age
print(get_name_with_age("Parit",18))


# Declaring types
# list
def process_items(items: list[str]):
    for item in items:
        print(item)

# in newer updates we can use list simply but before 3.6 we need to import the list in the code to use

# tuples and Set
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s
"""
The variable items_t is a tuple with 3 items, an int, another int, and a str.
The variable items_s is a set, and each of its items is of type bytes.
"""

#Dictionary
"""
To define a dict, you pass 2 type parameters, separated by commas.
The first type parameter is for the keys of the dict.
The second type parameter is for the values of the dict:
"""
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)
# here key type is rting and value type is float 

# Union
# You can declare that a variable can be any of several types, for example, an int or a str

def process_item(item: int | str):
    print(item)
# here item can be either int or string

#Possibly None
# You can declare that a value could have a type, like str, but that it could also be None.
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
# here it means the name can be their or not 

"""
Generic types
These types that take type parameters in square brackets are called Generic types or Generics like list , tuple
,set , dictionary and etc
"""

# Classes as types
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name  # this means "one_person is an instance of the class Person".

# Pydantic models
"""
Pydantic is a Python library used to **check and clean data**.
You create a class to show what your data should look like.
Each attribute in the class has a type (like `str`, `int`, etc.).

When you give values to that class, Pydantic:
Checks if the data is correct,
Converts it to the right type if needed,
And gives you a clean, ready-to-use object.
You also get help from your code editor, like autocomplete and error checks.
"""

from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []
external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# 123

# FastAPI are all based on Pydantic 

from typing import Annotated
name: Annotated[str, "SomeExtraInfo"] #The first part (str) is the real type. 
# The rest (SomeExtraInfo) is just extra metadata (extra info) — FastAPI can use it.
"""
What is Annotated?
Annotated is a special tool in Python. 
Python itself ignores it, but tools like FastAPI can use it to get extra info.

You can tell FastAPI things like:
"This field is required"
"This should be shown in the docs like this"
"This value must be greater than 0"
"""

"""
Type Hints in FastAPI
FastAPI uses Python type hints to:
Get editor support (autocomplete, suggestions)
Do type checking

And FastAPI uses these hints to:
Define request parameters (path, query, body, headers, etc.)
Convert request data to correct types
Validate data and return automatic errors if invalid
Auto-generate API docs (OpenAPI) with interactive UI
"""

# The important thing is that by using standard Python types, in a single place (instead of adding more classes,
# decorators, etc), FastAPI will do a lot of the work for you.
