import random
import datetime as dt
import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = '----'

def kelvin_to_fahrenheit(temp):
    celcius = temp - 273.15
    fahrenheit = (celcius * (9/5)) + 32
    return fahrenheit

def handle_response(message) -> str:
    print ('Handling response for message: ' + message)
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello, how are you?'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`!help - Shows this message`'

    #check the first 7 characters of the message
    if p_message[:7] == 'weather':
        #use the rest of the message as the city
        url = BASE_URL + '?appid=' + API_KEY + '&q=' + p_message[8:]
        print(url)
        response = requests.get(url).json()
        print (response)

        #make sure the json is valid
        if response['cod'] != 200:
            return 'Something went wrong with your request.'
        else:
            #process the response
            temp_response = response['main']['temp']
            temp_f = kelvin_to_fahrenheit(temp_response)
            temp_f = round(temp_f, 3)
            humidity = response['main']['humidity']
            description = response['weather'][0]['description']
            city = response['name']

            print(f"Weather in {city} is {description} with a temperature of {temp_f}°F and {humidity}% humidity.")
            return f"Weather in {city} is {description} with a temperature of {temp_f}°F and {humidity}% humidity."

    else:
        print ('No response found')