from kafka import KafkaConsumer
from weather_service import get_current_weather

KAFKA_BROKER_URL = 'http://host.docker.internal:29092/'
KAFKA_TOPIC = 'user-location-topic'

try:
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
    )
except Exception:
    print("Kafka unavailable")
    consumer = None

user_data = {}

if consumer:
    for message in consumer:
        event = message.value
        user_id = event['userID']
        location = event['location']
        timestamp = event['timestamp']

        weather = get_current_weather(location['lat'], location['lon'])
        user_data[user_id] = {
            'location': location,
            'timestamp': timestamp,
            'weather': weather
        }
