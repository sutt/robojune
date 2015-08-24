import os, sys, subprocess, time
from flask import Flask, send_file
import serial

sys.path.append(os.path.join(os.path.abspath('.'),"reqs", "imp"))
print sys.path
import myfunc

##GOAL: differentiate tty's and joystick turn on and read

devices = ['/dev/ttyACM0','/dev/ttyACM1']
baud = 115200
timeout = 10

#DOES: get pos preserve across closed connections?

def getpos():
	return 1

def smoothie(cmd):
		try:
			conn = serial.Serial(devices[1],baud,timeout=timeout)
			conn.write(str(cmd) + "\n")
			time.sleep(2)
			
			c = conn.write("get pos\n")
			out1 = conn.readlines()
			print out1.append("\n")
			conn.close()
		except:
			print 'not ', str(i)
			
	ret = " | ".join(out1)
	return ret 
  
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/smoothie/')
def reqsmoothie():
	return smoothie('')
	
@app.route('/smoothie/x/<data>')
def reqsmoothie(data):
	return smoothie("GO X"+str(data))
	  
if __name__== "__main__":
	app.run(host='0.0.0.0', threaded=True)
