import requests

def get_weather(city, api_key):
    """Fetch weather data from OpenWeather API for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description'].capitalize()

        print(f"\n🌍 Weather in {city_name}, {country}:")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌥️ Condition: {weather_desc}\n")

    else:
        print("\n❌ Error: Could not fetch weather data. Check the city name or API key.\n")


if __name__ == "__main__":
    print("=== 🌦️ Welcome to ClimaCheck 🌦️ ===")
    api_key = input("🔑 Enter your OpenWeatherMap API Key: ").strip()
    city = input("🏙️ Enter city name: ").strip()

    get_weather(city, api_key)
