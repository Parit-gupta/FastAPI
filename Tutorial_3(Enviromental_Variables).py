# You can create and use environment variables in the shell (terminal), without needing Python:
"""
Create an env var MY_NAME
$Env:MY_NAME = "Wade Wilson"

Use it with other programs, like
echo "Hello $Env:MY_NAME"

Hello Wade Wilson

"""

# You could also create environment variables outside of Python, in the terminal (or with any other method), 
# and then read them in Python.

import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")

"""
Environment variables are values you set outside the code, but your code can read them.
They're useful for things like:
Configurations (e.g., API keys, database URLs)
Keeping secrets out of your code and Git
You can also set them temporarily for one program run — and they disappear after it's done.
"""

# Just remember to name your path perfectly and never forget the basic functions of os as you can use it in this