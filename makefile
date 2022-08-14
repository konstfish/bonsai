build:
	docker-compose build

deploy:
	docker-compose up -d

logs:
	docker-compose logs -f