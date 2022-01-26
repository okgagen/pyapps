from gpiozero import LED
from gpiozero import PWMLED
from signal import pause
from time import sleep
from datetime import datetime
import random
import logging


now = datetime.now()
current_time = now.strftime("%H:%M:%S")

switch1 = LED(17)
switch2 = LED(27)

switch1.off()
switch2.off()


while True:
  now = datetime.now()
  stop_time = now.strftime("%H:%M")
#  print (stop_time)

  if current_time == "22:57":
    print("Good Night")

  else:
    switch1.on()
    switch2.blink()
    sleep(5)

    switch1.off()
    switch2.off()
    sleep(10)
