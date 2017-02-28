#!/bin/sh

kill `ps aux | grep rtmbot | awk '{ print $2 }' | head -1`

rm -rf "/yosbot"
