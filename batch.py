import os, sys, subprocess, time
from flask import Flask, send_file

import serial

sys.path.append(os.path.join(os.path.abspath('.'),"reqs", "imp"))
import myfunc
sys.path.append(os.path.join(os.path.abspath('.'),"arduapi", "arduino"))
import arduino

##GOAL - handle flask errors, turn joystick on!
	#can wait for a keyboard interupt, with an try/except wrapper

	#9:42 - added keyboard interup exception in req handling func wrapping the ardu poll loop. but creating the b object is still done on ini, so we expect this server to fail on 2nd request but to fail elegantly
	
devices = ['/dev/ttyACM0','/dev/ttyACM1']
baud = 115200
timeout = 10

b = arduino.Arduino('/dev/ttyACM0')
pin = 1

def joystick(data):
	ret = []
	#b.output([])
	for i in range(20):
		val = None
		try:
			val = b.analogRead(pin)
			print val
		except:
			print 'couldnt analogread'
			
		ret.append(val)
		print val
		time.sleep(0.5)
	return " | ".join(ret)

def getpos():
	return 1

def smoothie(cmd):
	ret = ""
	try:
		conn = serial.Serial(devices[1],baud,timeout=timeout)
		conn.write(str(cmd) + "\n")
		time.sleep(2)
		
		c = conn.write("get pos\n")
		out1 = conn.readlines()
		print out1.append("\n")
		conn.close()
		ret = " | ".join(out1)
	except:
		print 'not able to run cmd'
		
	
	return ret 
  
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/smoothie/')
def reqsmoothie():
	return smoothie('')
	
@app.route('/smoothie/x/<data>')
def reqsmoothiex(data):
	return smoothie("GO X"+str(data))

@app.route('/joystickon/')
def joystickon():	
	try:
		out = joystick([])
	except KeyboardInterrupt:
		print 'Interception!'
		try:
			sys.exit(0)
		except:
			os.exit(0)
	return out

if __name__== "__main__":
	app.run(host='0.0.0.0', threaded=True)
