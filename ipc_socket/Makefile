.PHONY: up down build
REG=smcsde
NAME=com
TAG=ipc_socket
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
	docker tag $(REG)/$(NAME):$(TAG)_server $(REG)/$(NAME):$(TAG)_server-$(VERSION)
	docker tag $(REG)/$(NAME):$(TAG)_client $(REG)/$(NAME):$(TAG)_client-$(VERSION)
	docker login
	docker push $(REG)/$(NAME):$(TAG)_server-$(VERSION)
	docker push $(REG)/$(NAME):$(TAG)_client-$(VERSION)
