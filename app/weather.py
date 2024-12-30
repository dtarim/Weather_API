import requests

def get_weather(city):
    api_key = "2b8c60edf455db374b33ce726d1899c0"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or 'cod' in data and data['cod'] != 200:
        # Hata durumunda dönecek yanıt
        return {"error": data.get("message", "An error occurred")}
    
    # Başarılı yanıt
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
