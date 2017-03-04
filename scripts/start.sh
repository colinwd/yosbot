#!/bin/bash

source ~/.yosenv/bin/activate

cd /yosbot
pip install -r requirements.txt

aws s3 cp s3://yosbot/config/rtmbot.conf /yosbot/rtmbot.conf
aws s3 cp s3://yosbot/config/weather.conf /yosbot/weather.conf

nohup rtmbot &>/dev/null &
