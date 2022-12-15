
up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build --no-cache

black:
	docker-compose run web black -S .