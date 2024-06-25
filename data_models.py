
from pydantic import BaseModel
from datetime import datetime


class WeatherData(BaseModel):
    temperature: str
    feels_like: int
    humidity: int
    condition: str


class Location(BaseModel):
    city: str
    lat: float
    lon: float


class UserData(BaseModel):
    location: Location
    timestamp: datetime
    weather: WeatherData


