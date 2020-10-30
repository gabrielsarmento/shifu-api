export PYTHONDONTWRITEBYTECODE=1


env = development


migrate:  # Run migrations
    PYTHONPATH=$(pwd) alembic upgrade HEAD

migrations:  # Create new migration from changes on models
    PYTHONPATH=$(pwd) alembic revision --autogenerate

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log
	@rm -f *.log.*

flake8:
	@flake8 --show-source .

check-python-import:
	@isort --check .

fix-python-import:
	@isort .

lint: clean flake8 check-python-import