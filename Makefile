.PHONY: install build run test tag push build-docker

IMAGE_NAME = reservation-system
TAG ?= latest

install:
	docker-compose run --rm web pip intall -r requirements.txt

build-docker:
	docker build -t ${IMAGE_NAME}:${TAG} .

run:
	docker-compose up web

test:
	docker-compose run --rm web pytest

tag:
	.

push:
	.

run-docker:
	docker run --network="host" -it -p 8000:8000 $(IMAGE_NAME):$(TAG)