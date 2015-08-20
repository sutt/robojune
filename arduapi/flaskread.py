import os, subprocess, time
from flask import Flask, send_file
import serial
import sys
import time

device = '/dev/ttyACM0'
baud = 115200
timeout = 3

from arduino import Arduino
import time

b = Arduino('/dev/ttyACM0')
pin = 1

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'
	
@app.route('/joystickon/')
def joystickon():
	
	ret = []
	b.output([])

	for i in range(10):
		val = None
		try:
			val = b.analogRead(pin)
		except:
			print 'couldnt analogread'
			
		ret.append(val)
		print val
		time.sleep(0.5)
	
	return " | ".join(ret)
	
