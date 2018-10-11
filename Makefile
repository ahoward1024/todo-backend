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

.EXPORT_ALL_VARIABLES:
	MONGO_DB_NAME=debug
	MONGO_DB_COLLECTION=debug_todo
	MONGO_DOMAIN=localhost
	MONGO_HEROKU=heroku
	MONGO_PASS=password
	MONGO_PORT=12345
	MONGO_USER=user

test:
	@echo 'Running tests'
	@echo $PATH
	pipenv run pytest --cov-report html --junit-xml=coverage.xml --cov-branch --cov-fail-under=90 -v --cov=tests/
