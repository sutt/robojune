import os, sys, subprocess, time
from flask import Flask, send_file

myGlobal = False
passIn = False

app = Flask(__name__)


@app.route('/ten/')
def ten(Flask.request()):
	print 'u'
	global myGlobal
	out = 0
	for i in range(10):
		if myGlobal & passIn:
			out = i
			break
			print passIn
		time.sleep(1)
	return str(out)

@app.route('/one/')
def one(passIn):
	global myGlobal
	myGlobal = True
	passIn = True
	return str(myGlobal)
	

@app.route('/')
def hello():
	return 'Hello World!'
	  
if __name__== "__main__":
	app.run(host='0.0.0.0', threaded=True)
