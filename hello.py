import os, subprocess, time
from flask import Flask, send_file
#import serial
import sys
import time

device = '/dev/ttyACM0'
baud = 115200
timeout = 3

def sendc(cmd):
  print "really in"
  global conn
  print cmd
  print cmd[0]
  conn.write(str(cmd) + "\n")
  #l =  conn.readlines()
  #print l
  #out2 = conn.readlines()
  print "done with sendc"
  return out2

def takepic(picid):
	picid += ".jpg"
	subprocess.call(["raspistill", "-o", picid])
	time.sleep(6)
	return picid
	
  
app = Flask(__name__)

@app.route('/ten/')
def ten():
	print 'here'
	time.sleep(10)
	return 'Yo'

@app.route('/one/')
def one():
	time.sleep(1)
	return 'one'

@app.route('/')
def hello():
	return 'Hello World!'
	
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
	app.run(host='0.0.0.0', threaded=True)
