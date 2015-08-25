import os, subprocess, time
from flask import Flask, send_file
import serial
import sys
import time
from arduino import Arduino


#device = '/dev/ttyACM0'
#baud = 115200
#timeout = 3

from arduino import Arduino
import time

def pollj():
	ret = []
	pin = 1	
	try:
		b = Arduino('/dev/ttyACM0')
		b.output([])
	except:
		print 'couldnt create b'

	for i in range(10):
		val = None
		try:
			val = b.analogRead(pin)
		except:
			print 'couldnt analogread ' + str(i)
		ret.append(val)
		print val
		time.sleep(0.5)
	return " | ".join(ret)


app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'
	
@app.route('/joystickon/')
def joystickon():
	try:
		out = pollj()
	except KeyboardInterrupt:
		print 'Interception!'
		try:
			sys.exit(0)
		except:
			os._exit(0)
	return out
	
if __name__== "__main__":
	app.run(host='0.0.0.0')
