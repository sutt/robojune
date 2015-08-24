import os, sys, subprocess, time
from flask import Flask, send_file
import sqlite3

myGlobal = False
passIn = False

app = Flask(__name__)


@app.route('/ten/')
def ten():
	print 'in ten'
	db = sqlite3.connect("db1.db")
	
	ini = db.cursor()
	ini.execute("""UPDATE tablet SET 'val' = 'Bad'""")
	db.commit()
	
	c = db.cursor()
	global myGlobal
	
	out = 0
	for i in range(15):
		c.execute("Select * from tablet")
		sql = c.fetchall()
		print sql
		if myGlobal == False: 
				print 'myGlobal=False'
		sqlBool = "Good" in sql[0]
		if myGlobal & sqlBool:
			out = i
			break
		time.sleep(1)
	db.close()
	return str(i)

@app.route('/one/')
def one():
	global myGlobal
	myGlobal = True
	return str(myGlobal)

@app.route('/two/')
def two():
	try:
		db = sqlite3.connect("db1.db")
	except:
		print 'no conn'
	c = db.cursor()
	c.execute("""UPDATE tablet SET 'val' = 'Good'""")
	db.commit()		#doesnt work get communicated to ten() without this line
	c2 = db.cursor()
	c2.execute("Select val from tablet")  #this can still get 'good'
	
	print "_" + str(c2.fetchall())
	db.close()
	return 'did it'

@app.route('/')
def hello():
	return 'Hello World!'
	  
if __name__== "__main__":
	app.run(host='0.0.0.0', threaded=True)
