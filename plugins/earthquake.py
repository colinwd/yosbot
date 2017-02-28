import json
import requests


def earthquake_in_bounds(lat, lon):
    min_lat = 42
    max_lat = 51
    min_lon = -123
    max_lon = -130
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon 


def grab_earthquake_feed():
    r = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson')
    return json.loads(r.text)['features']
            

def geo_filter(quakes):
    for quake in quakes:
        coords = quake['geometry']['coordinates']
        if earthquake_in_bounds(coords[1], coords[0]):
            yield quake
