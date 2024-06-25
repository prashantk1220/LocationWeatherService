import python_weather
import asyncio


async def fetch_weather(client, lat: float, lon: float):
    weather = await client.get(f"{lat},{lon}")
    return {
        'temperature': str(weather.temperature) + weather.unit.temperature,
        'feels_like': weather.feels_like,
        'humidity': weather.humidity,
        'condition': weather.description
    }


def get_current_weather(lat: float, lon: float):
    client = python_weather.Client()
    loop = asyncio.get_event_loop()
    weather_data = loop.run_until_complete(fetch_weather(client, lat, lon))
    loop.run_until_complete(client.close())
    return weather_data
