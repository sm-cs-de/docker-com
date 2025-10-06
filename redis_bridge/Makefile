.PHONY: up down build
REG=smcsde
NAME=com
TAG=redis_bridge
VERSION=latest
TOKEN=$(PWD)/../.access-token

build:
	docker compose build --pull

up:
	docker compose up -d

down:
	docker compose down

# see available images: docker images
# use command to tag and upload latest build: make VERSION=v2 upload
upload:
	docker tag $(REG)/$(NAME):$(TAG) $(REG)/$(NAME):$(TAG)-$(VERSION)
	@if [ ! -f $(TOKEN) ]; then \
		@cat $(TOKEN) | docker login -u $(REG) --password-stdin; \
	else \
		docker login; \
	fi
	docker push $(REG)/$(NAME):$(TAG)-$(VERSION)
