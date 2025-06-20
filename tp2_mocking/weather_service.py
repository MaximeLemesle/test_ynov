import requests  # type: ignore
import json
from datetime import datetime  # type: ignore


def get_temperature(city):
    """Récupère la température d'une ville via une API"""
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "fake_api_key",  # Clé bidon pour ce TP
        "units": "metric",
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["main"]["temp"]
        else:
            return None
    except requests.exceptions.RequestException:
        return None


def save_weather_report(city, filename="weather_log.json"):
    """Récupère la météo et la sauvegarde dans un fichier"""
    temp = get_temperature(city)
    if temp is None:
        return False
    report = {
        "city": city,
        "temperature": temp,
        "timestamp": datetime.now().isoformat(),
    }
    try:
        with open(filename, "r") as f:
            reports = json.load(f)
    except FileNotFoundError:
        reports = []
    reports.append(report)
    with open(filename, "w") as f:
        json.dump(reports, f)
    return True


print(get_temperature("Paris"))
