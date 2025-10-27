from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Automation & System Design Lab 🚀"}

@app.get("/weather", response_class=HTMLResponse)
def get_weather(city: str):
    """
    Fetch and display real-time weather for a given city as an HTML page.
    Example: http://127.0.0.1:8000/weather?city=London
    """
    # Step 1: Get latitude/longitude from city name
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()

    if not geo_data.get("results"):
        return f"<h2>❌ City '{city}' not found</h2>"

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    # Step 2: Get weather info
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    current = weather_data.get("current_weather", {})

    # Step 3: Build HTML dynamically
    html_content = f"""
    <html>
        <head>
            <title>Weather Report for {city}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                    text-align: center;
                    margin-top: 50px;
                }}
                .card {{
                    display: inline-block;
                    padding: 20px;
                    background: white;
                    border-radius: 10px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                }}
                h1 {{
                    color: #0078D7;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Weather in {city.title()}</h1>
                <p><b>Temperature:</b> {current.get("temperature")}°C</p>
                <p><b>Wind Speed:</b> {current.get("windspeed")} km/h</p>
                <p><b>Latitude:</b> {latitude}</p>
                <p><b>Longitude:</b> {longitude}</p>
                <p><i>Last Updated:</i> {current.get("time")}</p>
            </div>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content)
