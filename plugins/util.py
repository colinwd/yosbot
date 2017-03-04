#!/usr/bin/python
# -*- coding: utf-8 -*-


def c_to_f(temp):
    return format((float(temp) * 1.8) + 32, '.1f')


def format_weather_message(loc_string, temp_string, summary_string):
    response = {
        'attachments': [
            {
                'fallback': "Weather in {0} - {1}°C / {2}°F".format(loc_string, temp_string,
                                                                    c_to_f()),
                'pretext': "I found some weather, y'all...",
                'color': '#57FF57',
                'text': "Current weather for {0}".format(loc_string),
                'fields': [
                    {
                        'title': "Celsius",
                        'value': "{0}".format(temp_string),
                        'short': True
                    },
                    {
                        'title': "Fahrenheit",
                        'value': "{0}".format(c_to_f()),
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
