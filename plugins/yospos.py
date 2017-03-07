from rtmbot.core import Plugin
import requests
import json
import configparser


class WeatherPlugin(Plugin):
    """
        TODO:
        Store users and most recent queries in a hash table for 'default' lookup
        Check hash table for key of query to support looking up another user's weather
    """
    config = configparser.ConfigParser()
    config.read('weather.conf')
    dark_sky_key = config['default']['DarkSkyKey']

    def process_message(self, msg):
        if check_message(msg):
            channel = msg['channel']
            out_msg = self.weather_message(msg['text']);
            self.outputs.append([channel, out_msg])

    def weather_message(self, msg):
        loc = msg.lstrip('.wea').strip()
        coords = get_coordinates(loc)
        r = requests.get('https://api.darksky.net/forecast/{}/{},{}'.format(
            self.dark_sky_key, coords['lat'], coords['lon']),
            params={'units': 'si'})
        response = json.loads(r.text)
        message = "Current weather in " + coords['display_name'] + "\n"
        message += "Temperature: " + str(response['currently']['temperature']) + "C\n"
        message += response['currently']['summary']
        return message


def get_coordinates(loc):
    r = requests.get('http://nominatim.openstreetmap.org/search/' + loc,
                     params={'format': 'json', 'limit': 1})
    response = json.loads(r.text)
    return {'lat': response[0]['lat'], 'lon': response[0]['lon'], 'display_name': response[0]['display_name']}


def check_message(msg):
    return 'text' in msg and msg['text'].startswith('.wea')
