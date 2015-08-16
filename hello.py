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
  print "done with sendc"
  return 0

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'
	
@app.route('/takepic/')
def takepic():
	subprocess.call(["raspistill", "-o","newpic.jpg"])
	return 'pic taken'

@ap.route('/smoothie/')
def smoothie():
	conn = serial.Serial(device,baud,timeout=timeout)
	l = conn.write("get pos\n")
	print l
	ll = conn.readlines()
	print ll
	#" ".join(sys.argv[1:])
	sendc("")
	conn.close()
	
	
if __name__== "__main__":
	app.run(host='0.0.0.0')