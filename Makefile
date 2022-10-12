#!make
include .env

DOCKER_PROJECT_NAME := $(DOCKER_PROJECT_NAME)

export COMMIT_TAG=$(shell git describe --tags)
export LAST_VERSION_TAG=$(shell git describe --tags --abbrev=0)
export CODE_VERSION=$(shell git describe --dirty)

_DOCKER_COMPOSE_FILE=docker-compose.yml

DOCKER_COMPOSE=docker-compose -f $(_DOCKER_COMPOSE_FILE) -p $(DOCKER_PROJECT_NAME)

clean:
	@$(DOCKER_COMPOSE) down
	@$( $(shell docker ps -q --filter="name=$(DOCKER_PROJECT_NAME)") | docker stop )
	@$( $(shell docker ps -a -q --filter="name=$(DOCKER_PROJECT_NAME)") | docker rm )
	@$( $(shell docker images -q --filter="reference=*$(dDOCKER_PROJECT_NAME)*") | docker rmi )

run:
	$(DOCKER_COMPOSE) build
	$(DOCKER_COMPOSE) up -d --force-recreate --remove-orphans

logs:
	$(DOCKER_COMPOSE) logs -f -t

rl:
	$(MAKE) run
	$(MAKE) logs

admin:
	@$(DOCKER_COMPOSE) exec -it django python manage.py createsuperuser

makemigrations:
	@$(DOCKER_COMPOSE) exec -it django python manage.py makemigrations

makemessages:
	@$(DOCKER_COMPOSE) exec -it django django-admin makemessages -l pt_BR

compilemessages:
	@$(DOCKER_COMPOSE) exec -it django django-admin compilemessages

test:
	@$(DOCKER_COMPOSE) exec -it django python manage.py test

