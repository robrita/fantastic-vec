from fastapi import FastAPI, BackgroundTasks
import httpx
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file if it exists

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1/current.json"

async def get_weather_data(location: str):
    """Fetches current weather data from WeatherAPI."""
    async with httpx.AsyncClient() as client:
        params = {
            "key": WEATHER_API_KEY,
            "q": location,
            "aqi": "no"
        }
        try:
            response = await client.get(WEATHER_API_BASE_URL, params=params)
            response.raise_for_status()
            weather_data = response.json()
            return weather_data
        except httpx.HTTPError as e:
            print(f"Error fetching weather data: {e}")
            return None

async def background_weather_task(item_id: int, location: str):
    """Fetches weather data and processes it in the background."""
    print(f"Background weather task started for item_id: {item_id}")
    weather_info = await get_weather_data(location)
    if weather_info:
        location_name = weather_info["location"]["name"]
        condition = weather_info["current"]["condition"]["text"]
        temperature_c = weather_info["current"]["temp_c"]
        print(f"Weather in {location_name}: Condition: {condition}, Temperature: {temperature_c}°C")
    else:
        print(f"Could not retrieve weather data for {location}")
    print(f"Background weather task finished for item_id: {item_id}")


@app.post("/items/{item_id}")
async def create_item(item_id: int, background_tasks: BackgroundTasks):
    """Endpoint that returns immediately and runs a background weather task."""
    location = "Parañaque, Metro Manila, Philippines"
    background_tasks.add_task(background_weather_task, item_id, location)
    return {"message": "Item creation started with background weather update"}
