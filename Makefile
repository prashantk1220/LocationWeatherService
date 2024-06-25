.PHONY: all up start-kafka start-service down clean

all: up start-service

# Ready the env and Start the containers using docker-compose
up:
	@echo "Creating virtual env and installing dependencies..."
	python3 -m venv venv
	sh venv/bin/activate
	pip install -r requirements.txt
	@echo "Starting Kafka and Zookeeper containers..."
	docker-compose up -d
	@sleep 5

start-kafka:
	@echo "Setting up Kafka events..."
	docker exec -it kafka1 bash -c "\
		if ! kafka-topics --list --bootstrap-server localhost:9092 | grep -q 'user-location-topic'; then \
			kafka-topics --create --topic user-location-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1; \
		fi; \
		exit"
	python3 kafka_consumer.py

start-service:
	@echo "Starting User location-weather service..."
	python main.py

# Stop the containers
down:
	docker-compose down

# Stop the containers and remove volumes and dependencies
clean: down
	rm -rf venv
	docker-compose down -v --remove-orphans
	@sleep 5
