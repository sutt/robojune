import os, subprocess
from flask import Flask
import serial
import sys
import time

device = '/dev/ttyACM0'
baud = 115200
timeout = 3

def sendc(cmd):
  global conn
  conn.write(cmd + "\n")
  #l =  conn.readlines()
  #print l
  out2 = conn.readlines()
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
	conn = serial.Serial(device,baud,timeout=timeout)
	c = conn.write("get pos\n")
	out1 = conn.readlines()
	print ll
	out2 = sendc(str(data))
	conn.close()
	ret = [out1.join(" | ") ,out2.join(" | ")].join("\n")
	return ret 
	  
if __name__== "__main__":
	app.run(host='0.0.0.0')
