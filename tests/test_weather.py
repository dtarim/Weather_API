import pytest
from app.weather import get_weather

def test_get_weather():
    result = get_weather("Eindhoven")
    
    if "error" in result:
        # Hata mesajını doğrulayın
        assert result["error"] == "city not found" or "City not found" in result["error"]
    else:
        # Şehir bilgisini kontrol edin
        assert "city" in result
        assert "Eindhoven" in result["city"]  # Şehir adını içerip içermediğini kontrol edin
