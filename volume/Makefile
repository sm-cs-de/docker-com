.PHONY: up down build
REG=smcsde
NAME=com
TAG=volume
VERSION=latest
TOKEN=$(PWD)/../.access-token

up:
	docker compose up --build

upload:
	docker tag $(REG)/$(NAME):$(TAG)_writer $(REG)/$(NAME):$(TAG)_writer-$(VERSION)
	docker tag $(REG)/$(NAME):$(TAG)_reader $(REG)/$(NAME):$(TAG)_reader-$(VERSION)
	@if [ ! -f $(TOKEN) ]; then \
		@cat $(TOKEN) | docker login -u $(REG) --password-stdin; \
	else \
		docker login; \
	fi
	docker push $(REG)/$(NAME):$(TAG)_writer-$(VERSION)
	docker push $(REG)/$(NAME):$(TAG)_reader-$(VERSION)
