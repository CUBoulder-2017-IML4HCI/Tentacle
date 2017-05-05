from __future__ import print_function

from common import *
from myo_raw import MyoRaw

import OSC

wek = OSC.OSCClient()
wek.connect(('127.0.0.1', 6448))

tenta = OSC.OSCClient()
tenta.connect(('127.0.0.1', 12000))

def send(data, dest, address): 
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress(address)
    for elem in data:
            oscmsg.append(float(elem))
    
    dest.send(oscmsg)
    #if dest == wek:
    #print(oscmsg)
    #print(data)

def imu(quat,acc,gyro):
    #print(quat,acc,gyro)
    #print ("quat: ", quat, " type: ", type(quat))
    send(quat, wek, "/wek/inputs")

def pose(p):
    print(p) 
    
def emg(emg, moving): 
   emgdat = (sum(emg)/float(len(emg)),)
   #print ("emgdat: ", emgdat, " type: ", type(emgdat))
   send(emgdat, tenta, "/tenta_emg")
   

if __name__ == '__main__':
    
    m = MyoRaw()
    #m.add_imu_handler(print)    
    m.add_imu_handler(imu)
    #m.add_pose_handler(pose)
    m.add_emg_handler(emg)
    m.connect()
    while True:
        m.run()
