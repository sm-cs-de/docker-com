.PHONY: up down build
NAME=fastapi_rest
REG=smcsde
VERSION=latest

build:
	docker build . -t $(REG)/$(NAME)

up:
	docker run -d --name $(NAME) -p8080:8000 $(REG)/$(NAME)

down:
	docker stop $(NAME)
	docker rm $(NAME)

# see available images: docker images
# use command to tag and upload latest build: make VERSION=v2 upload
upload:
	docker tag $(REG)/$(NAME):latest $(REG)/$(NAME):$(VERSION)
	docker login
	docker push $(REG)/$(NAME):$(VERSION)
