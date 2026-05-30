import requests

def get_weather():

    url = "https://api.open-meteo.com/v1/forecast?latitude=15.2993&longitude=74.1240&current_weather=true"

    response = requests.get(url)

    return response.json()