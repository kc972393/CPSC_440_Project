#! /usr/bin/env python3
# CPSC-440 Project
# Brendan Wang and Katelyn Choi

import adafruit_dht
import time
import board

dhtSensor = adafruit_dht.DHT22(board.D4)

while True:
    try:
        humidity = dhtSensor.humidity
        temp_c = dhtSensor.temperature
    except RuntimeError:
        print("An error has occured, trying again.")
        continue

    print("The temperature is currently ", end="")
    print(temp_c, end="")
    print(" Celcius.")
    print("The humidity is currently ", end="")
    print(humidity, end="")
    time.sleep(60)