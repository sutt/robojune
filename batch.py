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
	
	#Failed to run once, could only be interrupt 1/2 times
	#9:51 - add the correct way to call b, 
	
	#this script could be interrupted by holding cntrl c without stop with five second delay for each operation that fails
	
	#error reports return from threading module, let
	
	#10:07: removing threading didnt work, now just write the code correctly...
	
	#10:12 we got it working on multiple requests 
	#can threading get added back in to allow interrupts - YES
	
	# build a:
		#joystickon = poll loop that calls smoothie
		#a secondary request that turns off joystick ability

thread_bool = False
if len(sys.argv) > 1:
	thread_bool = True

pollInt = False
	
devices = ['/dev/ttyACM0','/dev/ttyACM1']
baud = 115200
timeout = 3

def initsmoothie():
	conn = serial.Serial(devices[1],baud,timeout=timeout)
	return conn

def getpos(conn):
	
	conn.write("get pos\n")
	time.sleep(2)
	out = conn.readlines()
	out = filter(lambda e: 'Position' in e, out)[0]
	out = float(out[out.index("X:")+2 : out.index(",")])
	out += 17
	print out
	return str(out)
	
def buildgcode(val,pos):
	parseX = True
	if val > 530:
		return 1
	return 0

def pollj():
	ret = []
	pin = 1	
	
	global pollInt
	pollInt = False
	
	#conn = initsmoothie()

	try:
		b = arduino.Arduino('/dev/ttyACM0')
		b.output([])
		pin = 1
	except:
		print 'couldnt create b'

	for i in range(10):
		
		if pollInt:
			print 'pollInt'
			pollInt = False
			break
		
		try:
			val = None
			val = b.analogRead(pin)
			print val
			
		except:
			print 'couldnt analogread ' + str(i)

		#pos = getpos(conn)
		#gcode = buildgcode(val,pos)
		#smoothie(gcode)
		#ret.append((val,gcode))
		
		time.sleep(.5)
		ret.append(val)
		
	return " | ".join(ret)


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

@app.route('/getpos/')
def reqpos():
	conn = initsmoothie()
	out = getpos(conn)
	conn.close()
	return out
	
@app.route('/smoothie/')
def reqsmoothie():
	return smoothie('')
	
@app.route('/smoothie/x/<data>')
def reqsmoothiex(data):
	return smoothie("GO X"+str(data))

@app.route('/joystickon/')
def joystickon():	
	try:
		out = pollj()
	except KeyboardInterrupt:
		print 'Interception!'
		try:
			sys.exit(0)
		except:
			os.exit(0)
	return out
	
@app.route('/pollInt/')
def joystickoff():
	global pollInt
	pollInt = True
	return str(pollInt)

if __name__== "__main__":
	app.run(host='0.0.0.0', threaded=thread_bool)
