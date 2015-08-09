from arduino import Arduino
import time, sys, os

sys.argv

b = Arduino('/dev/ttyACM0')
pin = 1

b.output([])

while (True):
    val = b.analogRead(pin)
    print val
    time.sleep(0.5)