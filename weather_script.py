import requests

API_KEY = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': 'tempe',
        'appid': '72c1b3e9e22cbc7a39120dcd12cb94ee',
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print(f"Failed to get weather data for {city}. Error: {response.status_code}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)