define PRINT_HELP_PYSCRIPT

import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("	%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

PROJECT_NAME := bexs-banco
PYTHON_VERSION := 3.8.0
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

help:
	@echo "Usage: make <command> \n"
	@echo "options:"
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.pip:
	pip3 install --upgrade pip

.create-venv: ## Create virtual environment using pyenv and install requirements
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

.dev-requirements: ## Install all requirements for local development
	pip3 install -r requirements/development.txt

test: ## Run tests
	pytest --cov-report=term-missing --cov-report=html --cov=.

code-convention: ## Run code convention
	flake8 main.py app tests

install: .create-venv .pip .dev-requirements test code-convention ## Create venv, install dev requirements, run tests and code-convention

run-console: ## Run CLI application
	@pkill -9 python & python main.py --console

run-http-server: ## Run HTTP server application
	@pkill -9 python & python main.py
