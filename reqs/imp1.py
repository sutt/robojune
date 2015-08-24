#import imp.myfunc.MyClass as MC
import os, sys

sys.path.append(os.path.join(os.path.abspath('.'),"imp"))
#print sys.path
from myfunc import MyClass


print MyClass().func1()
