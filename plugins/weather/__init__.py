import configparser

config = configparser.ConfigParser()
config.read('weather.conf')
DARK_SKY_KEY = config['default']['DarkSkyKey']