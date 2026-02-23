.PHONY: help install install-dev test test-cov lint format run clean dist docs

help:
	@echo "FaceAttenDANCE - Comandos disponibles"
	@echo ""
	@echo "make install      Instalar dependencias"
	@echo "make install-dev  Instalar dependencias de desarrollo"
	@echo "make test         Ejecutar tests"
	@echo "make test-cov     Ejecutar tests con cobertura"
	@echo "make lint         Ejecutar linter"
	@echo "make format       Formatear código"
	@echo "make run          Ejecutar programa"
	@echo "make clean        Limpiar archivos temporales"
	@echo "make dist         Crear distribución"
	@echo "make docs         Generar documentación"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=src --cov-report=term --cov-report=html

lint:
	pylint src/

format:
	black src/ tests/

run:
	python src/main.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +

dist: clean
	python setup.py sdist bdist_wheel

docs:
	cd docs && mkdocs build