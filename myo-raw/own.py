from __future__ import print_function

from common import *
from myo_raw import MyoRaw

import OSC

wek = OSC.OSCClient()
wek.connect(('127.0.0.1', 6448))

def send(data): 
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/wek/inputs")
    for i,elem in enumerate(data):
            oscmsg.append(float(elem))
    
    wek.send(oscmsg)
    print(oscmsg)
    #print oscmsg[1:]
    print(data)

def imu(quat,acc,gyro):
    	#print(quat,acc,gyro)
    	print(quat,acc,gyro)
    	send(quat)

if __name__ == '__main__':
    
    m = MyoRaw()
    #m.add_imu_handler(print)    
    m.add_imu_handler(imu)
    m.connect()
    while True:
        m.run()
