# General
env:
	cp .env.template .env

# Django
createsuperuser:
	docker-compose run django bash -c "python3 manage.py createsuperuser"

makemigrations:
	docker-compose run django bash -c "python3 manage.py makemigrations"

migrate:
	docker-compose run django bash -c "python3 manage.py migrate"
