.PHONY: up down build

build:
	docker compose build --pull

up:
	docker compose up -d

down:
	docker compose down

# see available images: docker images
# use command to tag and upload latest build: make VERSION=v2 upload
upload:
	docker tag $(REG)/$(NAME):latest $(REG)/$(NAME):$(VERSION)
	docker login
	docker push $(REG)/$(NAME):$(VERSION)
