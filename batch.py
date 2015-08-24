import os, sys, subprocess, time
from flask import Flask, send_file
#import serial

sys.path.append(os.path.join(os.path.abspath('.'),"reqs", "imp"))
print sys.path
import myfunc

##GOAL: differentiate tty's and joystick turn on and read



	
  
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/newthing/')
def newthing():
	#from myfunc import MyClass
	reload(myfunc)
	return myfunc.MyClass.func1()
	  
if __name__== "__main__":
	app.run(host='0.0.0.0', threaded=True)
