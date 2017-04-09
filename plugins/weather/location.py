import requests
import json


def get_coordinates(loc):
    r = requests.get('http://nominatim.openstreetmap.org/search/' + loc,
                     params={'format': 'json', 'limit': 1})
    response = json.loads(r.text)

    return {
        'lat': response[0]['lat'],
        'lon': response[0]['lon'],
        'display_name': response[0]['display_name']
    }
