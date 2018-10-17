[![Build Status](https://travis-ci.org/ahoward1024/todo-backend.svg?branch=master)](https://travis-ci.org/ahoward1024/todo-backend)
[![codecov](https://codecov.io/gh/ahoward1024/todo-backend/branch/master/graph/badge.svg)](https://codecov.io/gh/ahoward1024/todo-backend)

# TODO BACKEND

A simple todo list written as an exercise in full stack development.
Written in Python using the Flask microframework.

# Initial setup

You will need three things to run the todo app:
- Python
- MongoDB

## Python
First you should set up a virtual environment. I personally used pipenv.
To set up for the first time use `pipenv install`

## MongoDB
Simply install MongoDB for your platform.

## Running

Set up the necessary environment variables (e.g.):
```
set FLASK_APP=runserver.py
set MONGO_DB_NAME=debug
set MONGO_DB_COLLECTION=debug_todo
set MONGO_DOMAIN=localhost
set MONGO_HEROKU=heroku
set MONGO_PASS=password
set MONGO_PORT=12345
set MONGO_USER=user
```

`pipenv shell` will open a subshell where you can then run `flask run`. The
server should be running at [http://localhost:5000](http://localhost:5000)
