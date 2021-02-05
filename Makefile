# General
env:
	cp .env.template .env

# Django
collect-static:
	docker-compose run django bash -c "python3 manage.py collectstatic"

create-sample-data:
	docker-compose run django bash -c "python3 manage.py createsampledata"

flush-and-create-sample-data:
	rm --force data/media/posters/*
	docker-compose run django bash -c "python3 manage.py createsampledata --flush"

create-super-user:
	docker-compose run django bash -c "python3 manage.py createsuperuser"

make-migrations:
	docker-compose run django bash -c "python3 manage.py makemigrations"

migrate:
	docker-compose run django bash -c "python3 manage.py migrate"

shell:
	docker-compose run django bash -c "python3 manage.py shell_plus"

test:
	docker-compose run django bash -c "python3 manage.py test"

# Docker
build:
	docker-compose build

up:
	docker-compose up

# React
install-ui-modules:
	cd frontend; npm install

start-ui-server:
	cd frontend; npm start
