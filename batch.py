import os, sys, subprocess, time
from flask import Flask, send_file
import serial

sys.path.append(os.path.join(os.path.abspath('.'),"reqs", "imp"))
print sys.path
import myfunc

##GOAL: differentiate tty's and joystick turn on and read

device = '/dev/ttyACM0'
baud = 115200
timeout = 10

def smoothie(cmd):
	conn = serial.Serial(device,baud,timeout=timeout)
	print "sending"
	conn.write(str(data) + "\n")
	time.sleep(2)
	
	c = conn.write("get pos\n")
	out1 = conn.readlines()
	print out1
	conn.close()
	
	ret = " | ".join(out1)
	return ret 
  
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/smoothie/')
smoothie('GO X1')
	  
if __name__== "__main__":
	app.run(host='0.0.0.0', threaded=True)
