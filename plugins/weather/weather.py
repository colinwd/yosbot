import requests
import json
import plugins.weather


def weather_message(location):
    response = get_weather(location['lat'], location['lon'])
    message = "Current weather in " + location['display_name'] + "\n"
    message += "Temperature: " + str(response['currently']['temperature']) + "C\n"
    message += response['currently']['summary']
    return message


def get_weather(lat, lon):
    r = requests.get('https://api.darksky.net/forecast/{}/{},{}'.format(
        plugins.weather.DARK_SKY_KEY, lat, lon),
        params={'units': 'si'})
    return json.loads(r.text)
