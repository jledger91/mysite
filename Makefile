# General
env:
	cp .env.template .env

# Django
collectstatic:
	docker-compose run django bash -c "python3 manage.py collectstatic"

createsuperuser:
	docker-compose run django bash -c "python3 manage.py createsuperuser"

makemigrations:
	docker-compose run django bash -c "python3 manage.py makemigrations"

migrate:
	docker-compose run django bash -c "python3 manage.py migrate"

shell:
	docker-compose run django bash -c "python3 manage.py shell_plus"

test:
	docker-compose run django bash -c "python3 manage.py test"
