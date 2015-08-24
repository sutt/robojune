import os, sys, subprocess, time
from flask import Flask, send_file

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
	  
if __name__== "__main__":
	app.run(host='0.0.0.0')
