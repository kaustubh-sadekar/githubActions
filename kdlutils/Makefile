PYTHON = python3

.PHONY = help setup test run clean
.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To build only python extension type make build"
	@echo "To build only python extension type make test"
	@echo "To build only python extension type make lint"
	@echo "------------------------------------"

build:
	@echo "=============================== \n"
	@echo "Installing library from source"
	@echo "=============================== \n"
	cd ../ && sudo ${PYTHON} setup.py install
	$(MAKE) lint
	$(MAKE) test

lint:
	@echo "================ \n"
	@echo "Lint with flake8 \n"
	@echo "================ \n"
	flake8 --per-file-ignores="__init__.py:F403,F401" && cd ../ && flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

test:
	@echo "============= \n"
	@echo "Running tests \n"
	@echo "============= \n"
	cd ../ && ${PYTHON} -m pytest


