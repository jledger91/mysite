# General
quick-install: env install-backend install-frontend

env:
	cp .env.template .env

# Docker
build:
	docker-compose build

up:
	docker-compose up

# Django
install-backend: build make-migrations migrate collect-static create-sample-data create-super-user

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

# React
install-frontend:
	cd frontend; npm ci

start-frontend:
	cd frontend; npm start

build-frontend:
	cd frontend; npm run build;
