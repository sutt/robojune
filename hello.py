import os, subprocess
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
  conn.write(cmd + "\n")
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
	c2 = sendc(str(data))
	c = conn.write("get pos\n")
	out1 = conn.readlines()
	#out2conn.readlines()
	conn.close()
	print "down to ret"
	#ret = [out1.join(" | ") ,out2.join(" | ")].join("\n")
	ret = out1.join(" | ")
	return ret 
	  
if __name__== "__main__":
	app.run(host='0.0.0.0')
