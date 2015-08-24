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

def smoothie(cmd):
	for i in range(2):
		print str(i)
		try:
			conn = serial.Serial(devices[i],baud,timeout=timeout)
			
			#conn.write(str(data) + "\n")
			#time.sleep(2)
			
			c = conn.write("get pos\n")
			out1 = conn.readlines()
			print out1
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
	return smoothie('GO X1')
	  
if __name__== "__main__":
	app.run(host='0.0.0.0', threaded=True)
