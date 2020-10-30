export PYTHONDONTWRITEBYTECODE=1


env = development


migrate:  # Run migrations
    PYTHONPATH=$(pwd) alembic upgrade HEAD

migrations:  # Create new migration from changes on models
    PYTHONPATH=$(pwd) alembic revision --autogenerate
