#!/usr/bin/python

import serial
import sys
import time

device = '/dev/ttyACM0'
baud = 115200

#  picocom --baud 115200 --echo --omap crlf --imap lfcrlf /dev/ttyACM0
# to exit: Cntrl+a Cntrl+q

#if len(sys.argv) > 1:
#    timeout = int(sys.argv[1])
#else:
#    timeout = 10
timeout = 3

conn = serial.Serial(device,baud,timeout=timeout)
l = conn.write("get pos\n")
print l
ll = conn.readlines()
print ll
#ll = conn.readline()
#ll += conn.readline()
#ll += conn.readline()
#print ll

def sendc(cmd):
  global conn
  conn.write(cmd + "\n")
  #l =  conn.readlines()
  #print l
  print "done with sendc"
  return 0

def readc(conn, timeout):
    return 1
  
sendc( " ".join(sys.argv[1:]) )
conn.close()
