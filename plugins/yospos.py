#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        message = format_weather_message(coords['display_name'], str(response['currently']['temperature']), response['currently']['summary'])
        return json.dumps(message)

def get_coordinates(loc):
    r = requests.get('http://nominatim.openstreetmap.org/search/' + loc,
                     params={'format': 'json', 'limit': 1})
    response = json.loads(r.text)
    return {'lat': response[0]['lat'], 'lon': response[0]['lon'], 'display_name': response[0]['display_name']}

def check_message(msg):
    return msg['text'].startswith('.wea')

def c_to_f(temp):
    return format((float(temp) * 1.8) + 32, '.1f')

def format_weather_message(loc_string, temp_string, summary_string):
    response = {
        'attachments': [
            {
                'fallback': "Weather in {0} - {1}°C / {2}°F".format(loc_string, temp_string, c_to_f(temp_string)),
                'pretext': "I found some weather, y'all...",
                'color': '#57FF57',
                'text': "Current weather for {0}".format(loc_string),
                'fields': [
                    {
                        'title': "Celcius",
                        'value': "{0}".format(temp_string),
                        'short': True
                    },
                    {
                        'title': "Farenheit",
                        'value': "{0}".format(c_to_f(temp_string)),
                        'short': True
                    },
                    {
                        'title': "Summary",
                        'value': "{0}".format(summary_string),
                        'short': False
                    }
                ]
            }
        ]
    }
    return response