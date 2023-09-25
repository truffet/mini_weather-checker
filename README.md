### README for Weather Information Python Script

#### Description:
This Python script fetches and displays the current weather information for a given city using the OpenWeatherMap API. It showcases the good use of APIs using the `requests` library in Python.

#### Requirements:
- Python
- requests library

To install the `requests` library, run the following command:
```sh
pip install requests
```

#### Usage:
1. Obtain an API key by signing up at [OpenWeatherMap](https://openweathermap.org/api).
2. Run the script.
3. Enter the API key and the name of the city when prompted.

#### How to Run:
```sh
python weather_script.py
```

#### Script Explanation:
- The script defines a function `get_weather` that takes an API key and a city name as parameters.
- It sends a GET request to the OpenWeatherMap API with the city name and API key.
- If the request is successful, it prints the weather description and temperature in Celsius for the given city.
- If the request fails, it prints the error code and error message.

#### Code Structure:
- The `get_weather` function is responsible for making the API request and handling the response.
- The `if __name__ == "__main__":` block is used to ensure that the script's main logic is only executed when the script is run directly and not when it is imported as a module.

#### Example:
```sh
Enter your OpenWeatherMap API Key: your_api_key
Enter the city: London
London: light rain - 12°C
```

#### Note:
- Handle API keys securely; avoid hardcoding them directly in the script.
- Be mindful of the API usage limits and terms of service of OpenWeatherMap.
- The script is intended for educational purposes to showcase the use of APIs using the `requests` library in Python.

### Final Thoughts:
This README provides the necessary information to understand, run, and utilize the weather information Python script. The script is a simple example demonstrating the interaction with a web API using Python and can be extended or modified for various use cases and other APIs.
