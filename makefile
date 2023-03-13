build:
	docker-compose --file docker-compose.dev.yml build

deploy:
	docker-compose --file docker-compose.dev.yml up -d

logs:
	docker-compose --file docker-compose.dev.yml logs -f

down:
	docker-compose --file docker-compose.dev.yml down -v

redeploy:
	docker-compose --file docker-compose.dev.yml down -v
	docker-compose --file docker-compose.dev.yml build
	docker-compose --file docker-compose.dev.yml up -d