help:
  @echo '  init'
  @echo '        install pipenv and dependencies'
  @echo '  test'
  @echo '        run pytest tests'

init:
  @echo 'Installing pipenv and all dependencies'
  pip install pipenv
  pipenv install

lint:
	@echo 'Linting code'
	pipenv run flake8

test:
  @echo 'Running tests'
  export FLASK_APP=runserver.py
  export MONOGO_DB_NAME=debug
  export MONGO_DB_COLLECTION=debug_todo
  export MONGO_DOMAIN=localhost
  export MONGO_HEROKU=heroku
  export MONGO_PASS=password
  export MONGO_PORT=12345
  export MONGO_USER=user
  pipenv run pytest --cov-report html --junit-xml=coverage.xml --cov-branch --cov-fail-under=90 -v --cov=tests/
