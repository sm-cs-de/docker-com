.PHONY: up down build
REG=smcsde
NAME=com
TAG=usb
VERSION=latest
TOKEN=$(PWD)/../.access-token

build:
	docker build . -t $(REG)/$(NAME):$(TAG)

up:
	docker run --device=/dev/bus/usb:/dev/bus/usb --privileged --name $(TAG) $(REG)/$(NAME):$(TAG)

down:
	docker stop $(TAG)
	docker rm $(TAG)

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
