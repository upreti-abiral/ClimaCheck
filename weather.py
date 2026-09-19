import requests


def get_weather(city, api_key):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"].capitalize()

        print(f"\nWeather in {city_name}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_desc}\n")

    except requests.exceptions.HTTPError:
        print("\nError: Could not find the city or access the weather data.\n")

    except requests.exceptions.RequestException:
        print("\nError: Could not connect to the weather service.\n")

    except (KeyError, ValueError):
        print("\nError: Unexpected weather data received.\n")


if __name__ == "__main__":
    print("=== ClimaCheck ===")

    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    city = input("Enter city name: ").strip()

    if not api_key:
        print("API key cannot be empty.")
    elif not city:
        print("City name cannot be empty.")
    else:
        get_weather(city, api_key)
