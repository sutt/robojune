import os, subprocess, time
from flask import Flask
import serial
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

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'
	
@app.route('/takepic/')
def takepic():
	subprocess.call(["raspistill", "-o","newpic.jpg"])
	return 'pic taken'

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
