.PHONY: up down build
REG=smcsde
NAME=com
TAG=ext_file
VERSION=latest

build:
	docker build . -t $(REG)/$(NAME):$(TAG)

up:
	docker run -v $(PWD)/file.txt:/app/mount/file.txt --name $(TAG) $(REG)/$(NAME):$(TAG)

down:
	docker stop $(TAG)
	docker rm $(TAG)

# see available images: docker images
# use command to tag and upload latest build: make VERSION=v2 upload
upload:
	docker tag $(REG)/$(NAME):$(TAG) $(REG)/$(NAME):$(TAG)-$(VERSION)
	docker login
	docker push $(REG)/$(NAME):$(TAG)-$(VERSION)
