import requests
import json
import pyttsx3

engine = pyttsx3.init()

def speak(text):
        engine.say(text)
        engine.runAndWait()

speak("Enter the name of the city: ")
city=input("Enter the name of the city: ")
url=f"https://api.weatherapi.com/v1/current.json?key=88d0b3210c2c4925b6184616251605&q={city}"

r=requests.get(url)

wdic=json.loads(r.text)
w=str(wdic["current"]["temp_c"])
print(f"The temperature of the city {city} is {w} degree celcius")
speak(f"The temperature of the city {city} is {w} degree celcius")

heat_index=str(wdic["current"]["heatindex_c"])
print(f"The heat index of {city} is {heat_index} in celcius")
speak(f"The heat index of {city} is {heat_index} in celcius")

weather_condition=str(wdic["current"]["condition"]["text"])
print(f"The weather condition of {city} is {weather_condition}")
speak(f"The weather condition of {city} is {weather_condition}")

humidity=str(wdic["current"]["humidity"])
print(f"The humidity of the city {city} is {humidity}")
speak(f"The humidity of the city {city} is {humidity}")