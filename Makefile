# General
quick-install: env build-frontend install-frontend install-backend

env:
	cp .env.template .env

# Docker
build:
	sudo docker-compose build

up:
	sudo docker-compose up

# Django
install-backend: build make-migrations migrate collect-static create-sample-data create-super-user

collect-static:
	sudo docker-compose run django bash -c "python3 manage.py collectstatic"

create-sample-data:
	sudo docker-compose run django bash -c "python3 manage.py createsampledata"

flush-and-create-sample-data:
	sudo rm --force data/media/posters/*
	sudo docker-compose run django bash -c "python3 manage.py createsampledata --flush"

create-super-user:
	sudo docker-compose run django bash -c "python3 manage.py createsuperuser"

make-migrations:
	sudo docker-compose run django bash -c "python3 manage.py makemigrations"

migrate:
	sudo docker-compose run django bash -c "python3 manage.py migrate"

shell:
	sudo docker-compose run django bash -c "python3 manage.py shell_plus"

test:
	sudo docker-compose run django bash -c "python3 manage.py test"

# React
install-frontend:
	cd frontend; npm ci

start-frontend:
	cd frontend; npm start

build-frontend:
	cd frontend; npm run build;
