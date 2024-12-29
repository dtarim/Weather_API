import pytest
from app.weather import get_weather

def test_get_weather():
    result = get_weather("London")
    assert "city" in result
    assert result["city"] == "London"
    assert "temperature" in result
    assert "description" in result
    assert "humidity" in result
