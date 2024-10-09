import requests #make a HHTP request to a web pagfe using python

import datetime #Import Datetime to convert Unix time to DateTime format

APIKey = '161f2b2f8004ff8ba8d21802d89edc48' #Enter your API key from the open Weather Website
BaseURL = "http://api.openweathermap.org/data/2.5/weather"

Greetings = 'Welcome to your Weather Tracker application, Which City do you want to view?'
print(Greetings)

# Input the relavant City Name
city = input('Enter a city Name: ')
RequestURL = f'{BaseURL}?appid={APIKey}&q={city}'
Response = requests.get(RequestURL)

#If the response is 'ok; then get the while JSOn Wather data as a Python dictonary

if Response.status_code == 200:
    Data = Response.json()
    weather = Data['weather'][0]['description']
    temprature = round(Data['main']['temp'] - 273.15,2)
    sunrise = datetime.datetime.utcfromtimestamp(Data['sys']['sunrise'] + Data['timezone'])
    sunset = datetime.datetime.utcfromtimestamp(Data['sys']['sunset'] + Data['timezone'])

    print('Weather Summary:',weather)
    print('The tempreture is:',temprature,'Celsius')
    print('The Sunrise time is:',sunrise)
    print('The sunset time is:',sunset)                             
else:
    print("Buddy..It doesn't look quite right, try again")

    
    

