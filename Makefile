include .env

# VARIABLES
# =============================================================================

DJANGO_RUN = $(call DOCKER_COMPOSE_RUN, django)

DOCKER_COMPOSE = sudo docker-compose

DOCKER_COMPOSE_EXEC = $(DOCKER_COMPOSE) exec $(1) bash -c

DOCKER_COMPOSE_RUN = $(DOCKER_COMPOSE) run --rm $(1) bash -c

MANAGE = python3 manage.py

NPM = cd frontend; npm

POSTGRES_EXEC = $(call DOCKER_COMPOSE_EXEC, postgres)

# COMMANDS
# =============================================================================

# General ---------------------------------------------------------------------

env:
	cp .env.template .env

quick-install: \
	env \
	install-frontend \
	build-frontend \
	install-backend

# Docker ----------------------------------------------------------------------

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up

# Django ----------------------------------------------------------------------

collect-static:
	$(DJANGO_RUN) "$(MANAGE) collectstatic"

create-sample-data:
	$(DJANGO_RUN) "$(MANAGE) createsampledata"

create-super-user:
	$(DJANGO_RUN) "$(MANAGE) createsuperuser"

flush-and-create-sample-data:
	-sudo rm --force data/media/posters/*
	$(DJANGO_RUN) "$(MANAGE) createsampledata --flush"

install-backend: \
	build \
	make-migrations \
	migrate \
	collect-static \
	create-sample-data \
	create-super-user

make-migrations:
	$(DJANGO_RUN) "$(MANAGE) makemigrations"

migrate:
	$(DJANGO_RUN) "$(MANAGE) migrate"

shell:
	$(DJANGO_RUN) "$(MANAGE) shell_plus"

test:
	$(DJANGO_RUN) "tox $(f)"

# Postgres --------------------------------------------------------------------

psql:
	$(POSTGRES_EXEC) "psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)"

# React -----------------------------------------------------------------------

build-frontend:
	$(NPM) run build

install-frontend:
	$(NPM) ci

start-frontend:
	$(NPM) start
