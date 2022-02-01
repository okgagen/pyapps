from gpiozero import LED
from gpiozero import PWMLED
from signal import pause
from time import sleep
from datetime import datetime
import random
import logging


now = datetime.now()
current_time = now.strftime("%H%M%S")


led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

led1.off()
led2.off()
led3.off()

ledpower = 0.5

sleeptime1 = 1
sleeptime2 = 5

while True:

  with open('somestat.txt') as f:
    somevalue = f.read()
    ledID = int(somevalue)
  f.close()

#  ledID = random.randint(1, 7)

  if ledID == 1:
    led1.value = ledpower
    sleep(sleeptime2)

    led1.off()
    sleep(sleeptime1)

  elif ledID == 2:
    led2.value = ledpower
    sleep(sleeptime2)

    led2.off()
    sleep(sleeptime1)

  elif ledID == 3:
    led3.value = ledpower
    sleep(sleeptime2)

    led3.off()
    sleep(sleeptime1)

  elif ledID == 4:
    led1.on()
    led2.on()
    sleep(sleeptime2)

    led1.off()
    led2.off()
    sleep(sleeptime1)

  elif ledID == 5:
    led1.on()
    led3.on()
    sleep(sleeptime2)

    led1.off()
    led3.off()
    sleep(sleeptime1)

  elif ledID == 6:
    led2.on()
    led3.on()
    sleep(sleeptime2)

    led2.off()
    led3.off()
    sleep(sleeptime1)

  else:
    led1.on()
    led2.on()
    led3.on()
    sleep(sleeptime2)

    led1.off()
    led2.off()
    led3.off()
    sleep(sleeptime1)
