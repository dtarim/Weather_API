from flask import Flask, jsonify
from app.weather import get_weather

app = Flask(__name__)

@app.route("/weather/<city>", methods=["GET"])
def weather(city):
    weather_info = get_weather(city)
    return jsonify(weather_info)

if __name__ == "__main__":
    app.run(debug=True)
