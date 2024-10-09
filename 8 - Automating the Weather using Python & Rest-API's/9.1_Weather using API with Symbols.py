import requests

APIKey = '161f2b2f8004ff8ba8d21802d89edc48'  # Enter your API key from OpenWeather
BaseURL = "http://api.openweathermap.org/data/2.5/weather"

greetings = 'Welcome to your Weather Tracker application. Which city do you want to view?'
print(greetings)

# Input the relevant city name
city = input('Enter a city name: ')
request_url = f'{BaseURL}?appid={APIKey}&q={city}&units=metric'  # Added units for temperature in Celsius
response = requests.get(request_url)

# If the response is 'ok', then get the whole JSON weather data as a Python dictionary
if response.status_code == 200:
    data = response.json()
    
    # Extract relevant information
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    icon_code = data['weather'][0]['icon']
    
    # Simple text-based representation of weather icons
    weather_symbols = {
        '01d': '☀️',  # Clear sky
        '01n': '🌙',  # Clear sky (night)
        '02d': '🌤️',  # Few clouds
        '02n': '🌥️',  # Few clouds (night)
        '03d': '☁️',  # Scattered clouds
        '03n': '☁️',  # Scattered clouds (night)
        '04d': '☁️',  # Broken clouds
        '04n': '☁️',  # Broken clouds (night)
        '09d': '🌧️',  # Shower rain
        '09n': '🌧️',  # Shower rain (night)
        '10d': '🌦️',  # Rain
        '10n': '🌧️',  # Rain (night)
        '11d': '⛈️',  # Thunderstorm
        '11n': '⛈️',  # Thunderstorm (night)
        '13d': '❄️',  # Snow
        '13n': '❄️',  # Snow (night)
        '50d': '🌫️',  # Mist
        '50n': '🌫️'   # Mist (night)
    }
    
    # Get the corresponding symbol
    weather_symbol = weather_symbols.get(icon_code, '🌈')  # Default to rainbow if not found

    print(f"Current temperature in {city}: {temperature}°C {weather_symbol}")
    print(f"Weather description: {weather_description}")

else:
    print("Buddy.. It doesn't look quite right, try again")
    print(f"Error Code: {response.status_code}, Message: {response.json().get('message', '')}")
