.PHONY: all up start-kafka start-service down clean

all: up start-kafka start-service

start-kafka:
	@echo "Setting up Kafka events..."
	docker exec -it locationweatherservice_kafka_1 bash -c "\
		if ! kafka-topics --list --bootstrap-server localhost:9092 | grep -q 'user-location-topic'; then \
			kafka-topics --create --topic user-location-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1; \
		fi; \
		exit"
	python kafka_consumer.py

start-service:
	@echo "Starting User location-weather service..."
	python main.py

# Start the containers using docker-compose
up:
	@echo "Starting Kafka and Zookeeper..."
	docker-compose up -d
	@sleep 5

# Stop the containers
down:
	docker-compose down

# Stop the containers and remove volumes
clean: down
	docker-compose down -v
