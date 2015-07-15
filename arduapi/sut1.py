import sys, optparse, time, math
from arduino import Arduino
import time, sys, os

p = optparse.OptionParser()
#p.add_option(

A = Arduino('/dev/ttyACM0')

def poll_ardu(ardu,pin):
    ardu.output([])
    return ardu.analogRead(pin)
    
def calibrate(ardu, **kwargs):
    cal_time = kwargs.get('cal_period',3)
    t_interval = kwargs.get('t_interval',.1)
    kwargs = kwargs.get('sigma',3)
    cal_steps = int( float(cal_time) / float(t_interval))
    m = []
    for i in range(cal_steps):
        d = poll_the_ardu(ardu,1)
        m.append(d)
        time.sleep(t_interval)
    sd = map(lambda x: (x - sum(m))^2, m)
    sd = math.sqrt( float(sd) / float(cal_steps) )
    print "-------------------------------"
    print sd
    return int(sd*sigma)

def monitor()
    #float(time_sleep)
    #t_interval = float(1) / float(pollhz)       
    #time.sleep(t_interval)
    return True

print "-------------------------------"
print calibrate()

    
 
