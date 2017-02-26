#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import yospos
import json

def test_c_to_f():
    assert yospos.c_to_f("32") == "89.6"
    assert yospos.c_to_f(32) == "89.6"
    assert yospos.c_to_f("0") == "32.0"
    assert yospos.c_to_f(-100) == "-148.0"

def test_format_weather_message():
    test_message = yospos.format_weather_message("upper yospos birch", "219", "Partly cloudy with a chance of Shaggars.")
    assert test_message['attachments'][0]['fields'][0]['value'] == "219"
    

