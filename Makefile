.PHONY: install-dev lint test build demo docker-build

install-dev:
	pip install -e ".[dev]"

lint:
	ruff check gamestar tests

test:
	pytest

build:
	python -m build

demo:
	python examples/practical_demo.py

docker-build:
	docker build -t gamestar:latest .
