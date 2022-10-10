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
	@$(DOCKER_COMPOSE) build
	@$(DOCKER_COMPOSE) up -d --force-recreate --remove-orphans
	$(MAKE) logs

db-load-backup:
	docker exec -i fdp_postgres pg_restore --verbose --clean --no-acl --no-owner -h localhost -U django -d django-db < ./database/init/backup

logs:
	@$(DOCKER_COMPOSE) logs -f -t
