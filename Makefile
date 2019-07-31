REPO_NAME = onsite-python3
PROJECT_NAME = myproj
PYTHON_VERSION = 3.7.4

REQUIREMENTS = $(wildcard requirements/*.in)
LOCKFILE = requirements/lock.txt


.DEFAULT: help
help:
	@echo "make init"
	@echo "    prepare development environment, use only once"
	@echo "make deinit"
	@echo "    remove all traces of virtual environment"
	@echo "make develop"
	@echo "    setup project for development"
	@echo "make reqs"
	@echo "make lock"
	@echo "    upgrade, lock, then install the Python dependencies in requirements/*.in"
	@echo "make lint"
	@echo "    run static checkers (i.e., flake8, bandit, safety, etc.)"
	@echo "make clean-py"
	@echo "    cleanup compiled Python files"
	@echo "make clean-venv"
	@echo "    remove virtual environment"


.PHONY: init
init: venv lock develop
	pip install --upgrade pip
	pip install --requirement $(LOCKFILE)
	@ pre-commit install --hook-type pre-commit || echo 'Install `pre-commit`!'
	@ pre-commit install --hook-type pre-push

.PHONY: deinit
deinit: clean-venv
	pyenv local --unset

.PHONY: develop
develop: venv
	python setup.py develop


venv: .python-version

.python-version:
	pyenv install --skip-existing $(PYTHON_VERSION)
	pyenv virtualenv $(PYTHON_VERSION) $(REPO_NAME)
	pyenv local $(REPO_NAME)

.PHONY: lock
lock: $(LOCKFILE)

.PHONY: reqs
reqs: lock

$(LOCKFILE): $(REQUIREMENTS)
	pip install --upgrade pip
	pip install pip-tools
	pip-compile --upgrade --generate-hashes --no-index --output-file $@ $(REQUIREMENTS)
	pip install --requirement $(LOCKFILE)


.PHONY: lint
lint:
	pre-commit run --all-files


.PHONY: test tests
tests: test
test: venv
	pytest


.PHONY: clean-py
clean-py:
	@ find . \
		-not \( -path "*/.git" -prune \) \
		\( -name '*.pyc' -or -name '*.pyo' -or -name '__pycache__' \) \
		-exec rm -vrf {} + 2>/dev/null \
			| wc -l \
			| xargs printf 'Removed %d compiled Python files\n'

.PHONY: clean-venv
clean-venv:
	pyenv uninstall --force $(PROJECT_NAME)
