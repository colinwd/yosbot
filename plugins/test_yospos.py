#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from .yospos import c_to_f, format_weather_message
import json

def test_c_to_f():
    assert c_to_f("32") == "89.6"
    assert c_to_f(32) == "89.6"
    assert c_to_f("0") == "32.0"
    assert c_to_f(-100) == "-148.0"

def test_format_weather_message():
    test_message = format_weather_message("upper yospos birch", "219", "Partly cloudy with a chance of Shaggars.")
    assert test_message['attachments'][0]['fields'][0]['value'] == "219"
    

