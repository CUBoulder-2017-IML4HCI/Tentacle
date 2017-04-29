from __future__ import print_function

from common import *
from myo_raw import MyoRaw
from twisted.internet import reactor, protocol
import OSC
import socket

wek = OSC.OSCClient()
wek.connect(('127.0.0.1', 6448))



def set_output(state):
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/wekinator/control/outputs")
    if state is 1:
        oscmsg.append(float(-1.0))
        oscmsg.append(float(1.0))
    elif state is 2:
        oscmsg.append(float(-1.0))
        oscmsg.append(float(-1.0))
    elif state is 3:
        oscmsg.append(float(1.0))
        oscmsg.append(float(1.0))
    elif state is 4:
        oscmsg.append(float(1.0))
        oscmsg.append(float(-1.0))
    wek.send(oscmsg)
    print(oscmsg)

def start_record():
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/wekinator/control/startRecording")
    wek.send(oscmsg)

def stop_record():
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/wekinator/control/stopRecording")
    wek.send(oscmsg)
    
def train():
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/wekinator/control/train")
    wek.send(oscmsg)    

def run():
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/wekinator/control/startRunning")
    wek.send(oscmsg)

def stop_run():
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/wekinator/control/stopRunning")
    wek.send(oscmsg)

def send(data): 
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/wek/inputs")
    for i,elem in enumerate(data):
            oscmsg.append(float(elem))
    
    wek.send(oscmsg)
    #print(oscmsg)
    #print oscmsg[1:]
    #print(data)

def imu(quat,acc,gyro):
    	#print(quat,acc,gyro)
    	#print(quat,acc,gyro)
    	send(quat)



class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print(data)
        data = data.strip()
        if(data == "1"):
            print("Recieved 1")
            set_output(1)
        elif(data == "2"):
            print("Recieved 2")
            set_output(2)
        elif(data == "3"):
            print("Recieved 3")
            set_output(3)
        elif(data == "4"):
            print("Recieved 4")
            set_output(4)
        elif(data == "5"):
            print("Recieved 5")
            start_record()
        elif(data == "6"):
            print("Recieved 6")
            stop_record()
        elif(data == "7"):
            print("Recieved 7")
            train()
        elif(data == "8"):
            print("Recieved 8")
            run()
        elif(data == "9"):
            print("Received 9")
            stop_run()
        reply = str(data) + "reply"
        self.transport.write(reply)    
        
        
  


if __name__ == '__main__':
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(10000,factory)
    reactor.run()
    
