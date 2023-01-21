build:
	docker-compose build

deploy:
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down -v

redeploy:
	docker-compose down -v
	docker-compose build
	docker-compose up -d