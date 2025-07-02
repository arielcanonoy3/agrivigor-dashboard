import requests

# Get coordinates of a location
def get_coords(location):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={location}"
    response = requests.get(url).json()
    if response:
        return float(response[0]["lat"]), float(response[0]["lon"])
    return None, None

# Fetch weather forecast using OpenWeather API
def fetch_forecast(lat, lon, api_key):
    url = (
        f"https://api.openweathermap.org/data/2.5/forecast?"
        f"lat={lat}&lon={lon}&appid={api_key}&units=metric"
    )
    response = requests.get(url)
    if response.ok:
        return response.json()
    return None

# Define risk rules and detect alerts
def analyze_weather(weather_data):
    alerts = []
    if not weather_data or "list" not in weather_data:
        return alerts

    high_humidity_threshold = 90
    rain_threshold = 20  # mm
    wind_threshold = 15  # m/s

    for entry in weather_data["list"][:8]:  # roughly 24h
        humidity = entry["main"]["humidity"]
        rain = entry.get("rain", {}).get("3h", 0)
        wind = entry["wind"]["speed"]

        if humidity > high_humidity_threshold:
            alerts.append("💧 High Humidity Stress")
        if rain > rain_threshold:
            alerts.append("🌧️Heavy Rain Risk")
        if wind > wind_threshold:
            alerts.append("💨Wind Damage Risk")
    return list(set(alerts))

