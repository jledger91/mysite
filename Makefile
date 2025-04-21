include .env

# VARIABLES
# =============================================================================

DJANGO_RUN = $(call DOCKER_COMPOSE_RUN, django)

DOCKER_COMPOSE = docker compose

DOCKER_COMPOSE_EXEC = $(DOCKER_COMPOSE) exec $(1)

DOCKER_COMPOSE_RUN = $(DOCKER_COMPOSE) run --rm $(1)

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
	$(DJANGO_RUN) collectstatic

create-sample-data:
	$(DJANGO_RUN) createsampledata

create-super-user:
	$(DJANGO_RUN) createsuperuser

flush-and-create-sample-data:
	-sudo rm --force data/media/posters/*
	$(DJANGO_RUN) createsampledata --flush

install-backend: \
	build \
	make-migrations \
	migrate \
	collect-static \
	create-sample-data \
	create-super-user

make-migrations:
	$(DJANGO_RUN) makemigrations

migrate:
	$(DJANGO_RUN) migrate

shell:
	$(DJANGO_RUN) shell_plus

test:
	$(DJANGO_RUN) tox $(f)

# Postgres --------------------------------------------------------------------

psql:
	$(POSTGRES_EXEC) psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

# React -----------------------------------------------------------------------

build-frontend:
	$(NPM) run build

install-frontend:
	$(NPM) ci

start-frontend:
	$(NPM) start
