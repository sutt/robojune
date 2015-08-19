import time, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
ss = .025

if len(sys.argv) > 1:
	steps = int(sys.argv[1])
else:
	steps = 50

if len(sys.argv) > 2:
	dirinp = GPIO.LOW
else:
	dirinp = GPIO.LOW

def rotate():
	sleep,dir,step = 7,3,5
	GPIO.setup(sleep, GPIO.OUT)
	GPIO.setup(dir, GPIO.OUT)
	GPIO.setup(step, GPIO.OUT)
	
	GPIO.output(sleep,GPIO.LOW)
	time.sleep(1.5)
	GPIO.output(sleep,GPIO.HIGH)
	
	time.sleep(.01)
	GPIO.output(dir,dirinp)
	time.sleep(.01)

	for i in range(steps):
		GPIO.output(step,GPIO.LOW)
		print i
		time.sleep(ss)
		GPIO.output(step,GPIO.HIGH)
		time.sleep(ss)

rotate()
