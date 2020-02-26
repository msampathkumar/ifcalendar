all: dependencies tests

.venv:  # creates .venv folder if does not exist
	python3 -mvenv .venv


.venv/bin/pip: .venv # installs latest pip
	.venv/bin/pip install -U pip setuptools


.venv/bin/nosetests: .venv/bin/pip  # ensures that test dependencies are installed (nose is a test runner)
	.venv/bin/pip install -r development.txt

# Runs the unit and functional tests
tests: .venv/bin/nosetests  # runs all tests
	.venv/bin/nosetests tests

# Install dependencies
dependencies: .venv
	.venv/bin/pip install -r development.txt

# runs unit tests

unit: .venv/bin/nosetests  # runs only unit tests
	.venv/bin/nosetests --cover-erase tests/unit

functional: .venv/bin/nosetests  # runs functional tests
	.venv/bin/nosetests tests/functional

cleanup:
	find . -name \*.pyc -delete

.PHONY: tests all unit functional run
