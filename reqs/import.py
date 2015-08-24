import os, sys, subprocess, time
from flask import Flask, send_file
#import imp.myfunc.func1

sys.path.append(os.path.join(os.getcwd() , 'imp'))
print sys.path

app = Flask(__name__)

@app.route('/func')
def func():
	print 'in here'
	return func1()
	

@app.route('/')
def hello():
	return 'Hello World!'
	  
if __name__== "__main__":
	app.run(host='0.0.0.0', threaded=True)
