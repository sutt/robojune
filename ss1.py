#!/usr/bin/python

import serial
import sys
import time

device = '/dev/ttyACM0'
baud = 115200

#  picocom --baud 115200 --echo --omap crlf --imap lfcrlf /dev/ttyACM0
# to exit: Cntrl+a Cntrl+q

timeout = 1

conn = serial.Serial(device,baud,timeout=timeout)

def sendc(cmd):
  global conn
  conn.write(cmd + "\n")
  time.sleep(1)
  return conn.readlines()
  
  
out = sendc( " ".join(sys.argv[1:]) )
print out
print '-----'

conn.close()
