.PHONY: migrations

migrations:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate