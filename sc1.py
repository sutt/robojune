#!/usr/bin/python

import serial
import sys
import time

device = '/dev/ttyACM0'
baud = 115200

conn = serial.Serial(device,baud)
l = conn.write("get pos\n")
print l
ll = conn.readline()
ll += conn.readline()
ll += conn.readline()
print ll

def sendc(cmd):
  global conn
  conn.write(cmd + "\n")
  l =  conn.readlines()
  print l
  return 0

sendc( " ".join(sys.argv[1:]) )
conn.close()
