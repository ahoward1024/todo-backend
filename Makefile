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
	@echo $$PATH
	pipenv run pytest --cov-report html --cov-report xml:codecov.xml --junit-xml=coverage.xml --cov-branch --cov-fail-under=90 -v --cov=server tests/
