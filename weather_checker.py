import requests

def get_weather(api_key, city):
  base_url = "http://api.openweathermap.org/data/2.5/weather"
  params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
  }
  response = requests.get(base_url, params=params)

  if response.status_code == 200:
    data = response.json()
    main = data['main']
    weather_description = data['weather'][0]['description']
    print(f"{city}: {weather_description} - {main['temp']}°C")
  else:
    print(f"Failed to get data: {response.status_code}")
    print(response.text)

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API Key: ")
    print(api_key)
    city = input("Enter the city: ")
    get_weather(api_key, city)
