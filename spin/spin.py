import os, subprocess, time
from flask import Flask, send_file
import serial
import sys
import time
import RPi.GPIO as GPIO

device = '/dev/ttyACM0'
baud = 115200
timeout = 3
GPIO.setmode(GPIO.BOARD)
ss = .05


def takepic(picid):
	picid += ".jpg"
	subprocess.call(["raspistill", "-o", picid])
	time.sleep(6)
	return picid
	
  
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/rotate/')
def rotate():
	sleep,dir,step = 7,3,5
	GPIO.setup(sleep, GPIO.OUT)
	GPIO.setup(dir, GPIO.OUT)
	GPIO.setup(step, GPIO.OUT)
	
	GPIO.output(sleep,False)
	time.sleep(ss)
	GPIO.output(sleep,True)
	
	
	for i in range(100):
		GPIO.output(step,True)
		time.sleep(ss)
		GPIO.output(step,True)
		time.sleep(ss)
	
	return 'done'
	
@app.route('/takepic/')
def reqtakepic():
	subprocess.call("ls")
	picid = 'takeit'
	fn = takepic(picid)
	subprocess.call("ls")
	return send_file(fn, mimetype='image/jpeg')

@app.route('/smoothie/<data>')
def smoothie(data):
	print "in"
	conn = serial.Serial(device,baud,timeout=timeout)
	print "sending"
	#c2 = sendc(str(data))
	conn.write(str(data) + "\n")
	time.sleep(2)
	c = conn.write("get pos\n")
	out1 = conn.readlines()
	print "before conn close"
	conn.close()
	print "down to ret"
	#ret = [out1.join(" | ") ,out2.join(" | ")].join("\n")
	print out1
	ret = " | ".join(out1)
	return ret 
	  
if __name__== "__main__":
	app.run(host='0.0.0.0')
