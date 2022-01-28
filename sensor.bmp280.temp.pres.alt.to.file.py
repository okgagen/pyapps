#!/usr/bin/env python3

import json
import time
from datetime import datetime
from bmp280 import BMP280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

#print("""Displays the temperature, pressure and altitude.

#Press Ctrl+C to exit!

#""")

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

baseline_values = []
baseline_size = 100

my_file="/home/pi/Documents/csv/bmp280.csv"
bmp280_csv = open(my_file, "w")
bmp280_csv.close()

for i in range(baseline_size):
    pressure = bmp280.get_pressure()
    baseline_values.append(pressure)
    time.sleep(1)

baseline = sum(baseline_values[:-25]) / len(baseline_values[:-25])
#print('Baseline: ', baseline)

while True:
    temperatureC = bmp280.get_temperature()
    temperatureF = temperatureC * 1.8 + 32
    pressure = bmp280.get_pressure()
    altitudeM = bmp280.get_altitude(qnh=baseline)
    altitudeF = altitudeM * 3.28084
    aline = json.dumps([datetime.now().strftime("%m:%d:%Y %H:%M:%S"), temperatureF, temperatureC, pressure, altitudeF, altitudeM])
    bmp280_csv = open(my_file, "a")
    bmp280_csv.write(aline)
    bmp280_csv.write('\n')
    bmp280_csv.close()
#    print(datetime.now(), 'Temperature: {:05.2f} *F, {:05.2f} *C, Pressure: {:05.2f} hPa, Altitude: {:05.2f} Ft, {:05.2f} meters'.format(temperatureF, temperatureC, pressure, altitudeF, altitudeM))
    time.sleep(1800)
