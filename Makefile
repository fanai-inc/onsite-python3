PROJECT_NAME = onsite-python3
PYTHON_VERSION = 3.7.4

REQUIREMENTS = $(wildcard requirements/*.in)
LOCKFILE = requirements/lock.txt


.DEFAULT: help
help:
	@echo "make init"
	@echo "    prepare development environment, use only once"
	@echo "make reqs"
	@echo "make lock"
	@echo "    upgrade, lock, then install the Python dependencies in requirements/*.in"
	@echo "make lint"
	@echo "    run static checkers (i.e., flake8, bandit, safety, etc.)"
	@echo "make clean-py"
	@echo "    cleanup compiled Python files"


init: venv lock
	pip install --requirement $(LOCKFILE)
	@ pre-commit install --hook-type pre-commit || echo 'Install `pre-commit`!'
	@ pre-commit install --hook-type pre-push

venv: .python-version

.python-version:
	pyenv install --skip-existing $(PYTHON_VERSION)
	pyenv virtualenv $(PYTHON_VERSION) $(PROJECT_NAME)
	pyenv local $(PROJECT_NAME)

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


.PHONY: clean-py
clean-py:
	@ find . \
		-not \( -path "*/.git" -prune \) \
		\( -name '*.pyc' -or -name '*.pyo' -or -name '__pycache__' \) \
		-exec rm -vrf {} + 2>/dev/null \
			| wc -l \
			| xargs printf 'Removed %d compiled Python files\n'
