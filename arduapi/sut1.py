import sys, os, optparse, time, math
from arduino import Arduino

p = optparse.OptionParser()
#p.add_option(

A = Arduino('/dev/ttyACM0')
A.output([])

def poll_ardu(ardu,pin):    
    return ardu.analogRead(pin)

def sd(obs):
    """returns sd [float] from obs [list] """
    n = len(obs)
    mean = float(sum(obs)) /  float(n)
    sd = map(lambda x: (x - mean)**2, m)
    retlsurn float(math.sqrt( float(sum(sd)) / float(n) ))

def calibrate(ardu, **kwargs):
    """returns tolerance [int] from Ardu sample """
    cal_time = kwargs.get('cal_period',3)
    t_interval = kwargs.get('t_interval',.5)
    kwargs = kwargs.get('sigma',3)
    cal_steps = int( float(cal_time) / float(t_interval))
    
    m = []
    for i in range(cal_steps):
        d = poll_ardu(ardu,1)
        m.append(int(d))
        time.sleep(t_interval)
    sd = sd(m)
    return int(sd*sigma)

def monitor():
    #float(time_sleep)
    #t_interval = float(1) / float(pollhz)       
    #time.sleep(t_interval)
    return True

print "-------------------------------"
cal = calibrate(A, cal_period = 5, t_interval = .2)
print cal

    
 
