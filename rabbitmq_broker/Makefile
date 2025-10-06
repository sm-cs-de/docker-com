.PHONY: up down build
REG=smcsde
NAME=com
TAG=rabbitmq_broker
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
	docker tag $(REG)/$(NAME):$(TAG)_producer $(REG)/$(NAME):$(TAG)_producer-$(VERSION)
	docker tag $(REG)/$(NAME):$(TAG)_consumer $(REG)/$(NAME):$(TAG)_consumer-$(VERSION)
	@if [ ! -f $(TOKEN) ]; then \
		@cat $(TOKEN) | docker login -u $(REG) --password-stdin; \
	else \
		docker login; \
	fi
	docker push $(REG)/$(NAME):$(TAG)_producer-$(VERSION)
	docker push $(REG)/$(NAME):$(TAG)_consumer-$(VERSION)
