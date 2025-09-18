.PHONY: up down build
REG=smcsde
NAME=com
TAG=volume
VERSION=latest

up:
	docker compose up --build

upload:
	docker tag $(REG)/$(NAME):$(TAG)_writer $(REG)/$(NAME):$(TAG)_writer-$(VERSION)
	docker tag $(REG)/$(NAME):$(TAG)_reader $(REG)/$(NAME):$(TAG)_reader-$(VERSION)
	docker login
	docker push $(REG)/$(NAME):$(TAG)_writer-$(VERSION)
	docker push $(REG)/$(NAME):$(TAG)_reader-$(VERSION)
