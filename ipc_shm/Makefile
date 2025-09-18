.PHONY: up down build
REG=smcsde
NAME=com
TAG=ipc_shm
VERSION=latest

build:
	docker compose build --pull

up:
	docker compose up -d

down:
	docker compose down

# see available images: docker images
# use command to tag and upload latest build: make VERSION=v2 upload
upload:
	docker tag $(REG)/$(NAME):$(TAG)_writer $(REG)/$(NAME):$(TAG)_writer-$(VERSION)
	docker tag $(REG)/$(NAME):$(TAG)_reader $(REG)/$(NAME):$(TAG)_reader-$(VERSION)
	docker login
	docker push $(REG)/$(NAME):$(TAG)_writer-$(VERSION)
	docker push $(REG)/$(NAME):$(TAG)_reader-$(VERSION)
