import plugins.weather.weather as weather
import plugins.weather.location as location
from rtmbot.core import Plugin


class WeatherPlugin(Plugin):
    """
        TODO:
        Store users and most recent queries in a hash table for 'default' lookup
        Check hash table for key of query to support looking up another user's weather
    """

    def process_message(self, msg):
        if check_message(msg):
            channel = msg['channel']
            loc_string = msg.lstrip('.wea').strip()
            coords = location.get_coordinates(loc_string)
            out_msg = weather.weather_message(coords)
            self.outputs.append([channel, out_msg])


def check_message(msg):
    return 'text' in msg and msg['text'].startswith('.wea')
