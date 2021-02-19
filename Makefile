# Vars
DJANGO_RUN = $(DOCKER_COMPOSE) run django bash -c
DOCKER_COMPOSE = sudo docker-compose
MANAGE = python3 manage.py
NPM = cd frontend; npm

# General
quick-install: \
	env \
	install-frontend \
	build-frontend \
	install-backend

env:
	cp .env.template .env

# Docker
build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up

# Django
install-backend: \
	build \
	make-migrations \
	migrate \
	collect-static \
	create-sample-data \
	create-super-user

collect-static:
	$(DJANGO_RUN) "$(MANAGE) collectstatic"

create-sample-data:
	$(DJANGO_RUN) "$(MANAGE) createsampledata"

flush-and-create-sample-data:
	sudo rm --force data/media/posters/*
	$(DJANGO_RUN) "$(MANAGE) createsampledata --flush"

create-super-user:
	$(DJANGO_RUN) "$(MANAGE) createsuperuser"

make-migrations:
	$(DJANGO_RUN) "$(MANAGE) makemigrations"

migrate:
	$(DJANGO_RUN) "$(MANAGE) migrate"

shell:
	$(DJANGO_RUN) "$(MANAGE) shell_plus"

test:
	$(DJANGO_RUN) "$(MANAGE) test"

# React
install-frontend:
	$(NPM) ci

start-frontend:
	$(NPM) start

build-frontend:
	$(NPM) run build
