import python_weather
import asyncio


async def fetch_weather(client, lat: float, lon: float):
    weather = await client.get(f"{lat},{lon}")
    return {
        'temperature': weather.current.temperature,
        'feels_like': weather.current.feels_like,
        'humidity': weather.current.humidity,
        'condition': weather.current.sky_text
    }


def get_current_weather(lat: float, lon: float):
    client = python_weather.Client(format=python_weather.METRIC)
    loop = asyncio.get_event_loop()
    weather_data = loop.run_until_complete(fetch_weather(client, lat, lon))
    loop.run_until_complete(client.close())
    return weather_data
