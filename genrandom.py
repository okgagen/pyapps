import random
from time import sleep

while True:

  ledID = random.randint(1, 7)
  ledID = str(ledID)
  f = open('somestat.txt', 'w')
  f.write(ledID)
  f.close()
  sleep(4)
