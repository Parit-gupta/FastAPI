"""
Main Commands
Here are the primary commands you'll use:

Creating a Virtual Environment:

python -m venv venv

Explanation:
python -m venv: This invokes the venv module (part of Python's standard library) to create a virtual environment.
venv: This is the chosen name for your virtual environment directory. You can name it anything you like (e.g., .venv, myenv), but venv is a common convention. This command creates a directory named venv in your current project directory.
Activating the Virtual Environment:

.\venv\Scripts\Activate.ps1

Explanation:
Activation modifies your shell's PATH variable so that when you run python or pip, it refers to the 
executables within your virtual environment, not your global Python installation.
You'll typically see the name of your virtual environment (e.g., (venv)) prepended to your command prompt, 
indicating that it's active.

Installing FastAPI (and Uvicorn) within the Virtual Environment:

pip install fastapi uvicorn

Explanation:
Once your virtual environment is active, pip refers to the pip within that environment.
This command installs FastAPI and Uvicorn (an ASGI server often used to run FastAPI applications) 
specifically into your active virtual environment. They won't be installed globally.

Deactivating the Virtual Environment:

deactivate

Explanation:
This command reverts your shell's PATH variable, taking you out of the virtual environment and back to your 
system's global Python. The (venv) prefix will disappear from your prompt.
Generating a requirements.txt file:

pip freeze > requirements.txt

Explanation:
pip freeze: This command lists all the packages installed in the current active virtual environment along with 
their exact versions.

> requirements.txt: This redirects the output of pip freeze into a file named requirements.txt. This file is 
crucial for sharing your project and for others to recreate your environment.
Installing Dependencies from requirements.txt:

pip install -r requirements.txt

Explanation:
This command reads the requirements.txt file and installs all the listed packages with their specified versions
into the active virtual environment. This is how others (or you on a different machine) can set up the exact 
same development environment.
"""
"""
Why use a virtual environment (venv)? :
A virtual environment is used to create a separate space for your project's 
dependencies so they don’t conflict with other projects or the system Python.
"""

