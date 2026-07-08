import requests


class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, **params):
        params["appid"] = self.api_key
        params["units"] = "metric"

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            return response.json()

        return None

    def display_weather(self, data):
        print("\n------ Weather Report ------")
        print("Description :", data["weather"][0]["description"])
        print("Temperature :", data["main"]["temp"], "°C")
        print("Feels Like  :", data["main"]["feels_like"], "°C")
        print("Humidity    :", data["main"]["humidity"], "%")
        print("Wind Speed  :", data["wind"]["speed"], "m/s")
API_KEY = "12df24494f2795d19536f8f286d9d3d1"
weather = WeatherAPI(API_KEY)
choice = input("1. Search by City\n2. Search by Coordinates\nChoose: ")

if choice == "1":
    city = input("City: ")
    country = input("Country Code: ")

    data = weather.get_weather(q=f"{city},{country}")

elif choice == "2":
    lat = input("Latitude: ")
    lon = input("Longitude: ")

    data = weather.get_weather(lat=lat, lon=lon)

else:
    data = None

if data:
    weather.display_weather(data)
else:
    print("Unable to fetch weather.")