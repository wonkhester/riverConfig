#!/usr/bin/env python3

import requests
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=os.path.expanduser("~/.config/waybar/scripts/.env"))

API_KEY = os.getenv("WEATHER_API_KEY")
LOCATION = os.getenv("LOCATION")

WEATHER_ICONS = {
    "Sunny": "☀️",
    "Partly cloudy": "⛅",
    "Cloudy": "☁️",
    "Overcast": "☁️",
    "Mist": "🌫️",
    "Fog": "🌫️",
    "Patchy rain possible": "🌦️",
    "Light rain": "🌧️",
    "Moderate rain": "🌧️",
    "Heavy rain": "🌧️",
    "Thunderstorm": "⛈️",
    "Patchy snow possible": "🌨️",
    "Light snow": "🌨️",
    "Moderate snow": "🌨️",
    "Heavy snow": "❄️",
}

def get_weather():
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}&aqi=no"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    icon = WEATHER_ICONS.get(condition, "❓")
    return icon, temp_c, condition

def main():
    try:
        icon, temp, condition = get_weather()

        # Detect mode
        mode = sys.argv[1] if len(sys.argv) > 1 else "full"

        if mode == "icon":
            print(f'{{"text": "{icon}", "tooltip": "{condition}"}}')
        elif mode == "info":
            print(f'{{"text": "{temp}°C", "tooltip": "{condition}"}}')
        else:
            print(f'{{"text": "{icon} {temp}°C", "tooltip": "{condition}"}}')
    except Exception as e:
        print(f'{{"text": "⚠️", "tooltip": {e}}}')

if __name__ == "__main__":
    main()

