import requests
from flask import Flask, jsonify

API_KEY = "2b8c60edf455db374b33ce726d1899c0"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return {"error": "City not found"}
