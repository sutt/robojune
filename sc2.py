#!/usr/bin/python

import serial
import sys
import time
import subprocess

device = '/dev/ttyACM0'
baud = 115200

#  picocom --baud 115200 --echo --omap crlf --imap lfcrlf /dev/ttyACM0
# to exit: Cntrl+a Cntrl+q

conn = serial.Serial(device,baud,timeout=timeout)

def sendc(cmd):
  global conn
  conn.write(cmd + "\n")
  #l =  conn.readlines()
  #print l
  print "done with sendc"
  return 0

def readc(conn, timeout):
    return 1

sendc( "get pos \n")
time.sleep(.1)

for i in range(10):
	step = .01* i 
	sendc("G0 Z" + str(step))
	print i
	time.sleep(.1)

print 'done'
conn.close()
