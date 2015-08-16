import time
import RPi.GPIO as GPIO

def rotate():
	sleep,dir,step = 7,3,5
	GPIO.setup(sleep, GPIO.OUT)
	GPIO.setup(dir, GPIO.OUT)
	GPIO.setup(step, GPIO.OUT)
	
	GPIO.output(sleep,GPIO.LOW)
	time.sleep(ss)
	GPIO.output(sleep,GPIO.HIGH)
	
	
	for i in range(100):
		GPIO.output(step,GPIO.LOW)
		time.sleep(ss)
		GPIO.output(step,GPIO.HOGH)
		time.sleep(ss)

rotate()