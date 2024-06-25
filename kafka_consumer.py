from kafka import KafkaConsumer
from weather_service import get_current_weather
from datetime import datetime


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


user_data = {81325: {
    "location": {'city': 'Berlin', 'lat': 52.520008, 'lon': 13.404954},
    "weather": get_current_weather(52.520008, 13.404954),
    "timestamp": datetime.now()
}}


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
