PYTHON = python3

.PHONY = help setup test run clean
.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To build only python extension type make build"
	@echo "To build only python extension type make test"
	@echo "------------------------------------"

build:
	@echo "=============================================== \n"
	@echo "Installing omnicv python library from source"
	@echo "=============================================== \n"
	cd ../ && sudo ${PYTHON} setup.py install
	@echo "Running tests for Python extension \n"
	@echo "=============================================== \n"
	$(MAKE) test

test:
	@echo "=============================================== \n"
	@echo "Running tests for Python extension \n"
	@echo "=============================================== \n"
	cd ../ && ${PYTHON} -m pytest


