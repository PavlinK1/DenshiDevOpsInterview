.PHONY: up down build

build:
	docker-compose build

up:
	docker-compose up -d

test:
	docker-compose run --rm todo-app npm test

clean:
	docker-compose down