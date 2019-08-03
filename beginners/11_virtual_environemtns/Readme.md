# Python Virtual Environments
A virtual environment is a place on your system where you can install packages and isolate
them from all other Python packages. Separating one project’s libraries from other projects is beneficial and will be necessary when we deploy large projects
## Install Virtual Environment binary 
    $ pip install virtualenv
## Creating Virtual Environment
    $ virtualenv demo-venv
## Activate Virtual Environment
    $ source ./bin/activate
## Install libraries specific to Virtual Environment
    $ pip install requests
## List libraries specific to Virtual Environment
    $ pip list
## Create requirements libraries specific to virtual Environment
    $ pip freeze > requirements.txt
## Deactivate Environment
    $ deactivate
## Install the dependencies from requirements file
    $pip install -r requirements.txt
