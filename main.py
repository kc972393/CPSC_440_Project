#! /usr/bin/env python3
# CPSC-440 Project
# Brendan Wang and Katelyn Choi

import adafruit_dht
import time
import board
import espeakng

dhtSensor = adafruit_dht.DHT22(board.D4, False)
esng = espeakng.Speaker()

while True:
    try:
        humidity = dhtSensor.humidity
        temp_c = dhtSensor.temperature
    except RuntimeError:
        continue

    print("The temperature is currently ", end="")
    print(temp_c, end="")
    print(" degrees Celcius.")
    print("Humidity: ", end="")
    print(humidity)
    print("==============================")
    converted_num = str(temp_c)
    esng.say(converted_num, wait4prev=True)
    esng.say('degrees celsius', wait4prev=True)
    time.sleep(10)