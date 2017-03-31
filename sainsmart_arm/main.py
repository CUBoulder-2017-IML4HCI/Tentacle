import OSC
import time
import os
import socket
from OSC import OSCClient, OSCMessage
from OSC import OSCServer
import collections

server = OSCServer( ("localhost", 12000) )
server.timeout = 0
run = True

# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False
def handle_timeout(self):
    self.timed_out = True

# funny python's way to add a method to an instance of a class
import types
server.handle_timeout = types.MethodType(handle_timeout, server)

import serial
ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

#server.addMsgHandler("/wek/outputs",response)

def sendserial(motor,value):
	print "Inside sendserial"
	mot = ord('A')+ motor
	str1 = chr(mot)+str(value)
	print str1
	ser.write(str1)
	feedback = ser.readline()
	print feedback
	[feed_mot,feed_val] = feedback.split('=')
	print feed_mot,feed_val
	while ((int(feed_mot)!=motor) or (int(feed_val)!=value)):
		ser.write(str1)
		feedback = ser.readline()
		print feedback
		[feed_mot,feed_val] = feedback.split('=') 
		print feed_mot,feed_val



class Motion:
    def __init__(self):
        
        #motor contraint vars.
        self.m1 = 60
        self.m2 = 60
        self.m3 = 60
        self.m4 = 60
        self.m5 = 0
        self.m6 = 0

        #A
        self.l_m1 = 0
        self.u_m1 = 180

        #B	
        self.l_m2 = 20
        self.u_m2 = 130

        self.l_m3 = 20
        self.u_m3 = 160

        self.l_m4 = 0
        self.u_m4 = 180

        self.l_m5 = 0
        self.u_m5 = 180
        self.l_m6 = 0
        self.u_m6 = 180

        #Input a default position for the arm
        sendserial(0,self.m1)
        sendserial(1,self.m2)
        sendserial(2,self.m3)
        sendserial(3,self.m4)
        sendserial(4,self.m5)
        sendserial(5,self.m6)

    def left(self):
    	self.m1 = self.m1-5
    	if(self.m1 < 0):
    		self.m1 = 0

    	sendserial(0,self.m1)
    	'''
    	var = 'A' + str(self.m1)
    	print var
    	ser.write(var)
    	'''
    def right(self):
    	self.m1 = self.m1+5
    	if(self.m1 > 180):
    		self.m1 = 180
    	sendserial(0,self.m1)
    	'''
    	var = 'A' + str(self.m1)
    	print var
    	ser.write(var)
		'''
    def up(self):
    	self.m3 = self.m3+5
    	self.m2 = 180-self.m3-30

    	if(self.m2 < 0):
    		self.m2 = 0
    	if(self.m2 > 130):
    		self.m2 = 130
    	if(self.m3 > 160):
    		self.m3 = 160
    	sendserial(2,self.m3)
    	sendserial(1,self.m2)
    	
    def down(self):
    	self.m3 = self.m3-5
    	self.m2 = 180-self.m3-30

    	if(self.m2 < 0):
    		self.m2 = 0
    	if(self.m2 > 130):
    		self.m2 = 130
    	if(self.m3 < 0):
    		self.m3 = 0
    	sendserial(2,self.m3)
    	sendserial(1,self.m2)

    # Does not work!
    def joint1_up(self):
    	self.m4 = self.m4+5
    	if(self.m4 > 180):
    		self.m4 = 180
    	sendserial(3,self.m4)

    #Does not work!
    def joint1_down(self):
    	self.m4 = self.m4-5
    	if(self.m4 < 0):
    		self.m4 = 0
    	sendserial(3,self.m4)

    def joint2_up(self):
    	self.m5 = self.m5+5
    	if(self.m5 > 180):
    		self.m5 = 180
    	sendserial(4,self.m5)

    def joint2_down(self):
    	self.m5 = self.m5-5
    	if(self.m5 < 0):
    		self.m5 = 0
    	sendserial(4,self.m5)
    	
motion = Motion()

def respond_motion(value):

	print "Initialized respond"


	global current_output
	print "\nResponse Generating"
	
	if value == 2.0 :
		print "Left"
		motion.left()
	elif value == 3.0 :
		print "Right"
		motion.right()
	elif value == 4.0 :
		print "Up"
		motion.up()
	elif value == 5.0 :
		print "Down"
		motion.down()
	elif value == 6.0 :
		print "Joint1_up"
		motion.joint1_up()
	elif value == 7.0 :
		print "Joint1_down"
		motion.joint1_down()
	elif value == 8.0 :
		print "Joint2_up"
		motion.joint2_up()
	elif value == 9.0 :
		print "Joint2_down"
		motion.joint2_down()
	elif value == 1.0 :
		print "Stay"
		pass
		#motion.right()
                '''
	if d[0] == 3.0 :
		print "Obstacle"
		speech('Obstacle')
		current_output = 3.0
                
                if d[0] == 4.0 :
		print "Straight"
		speech('Straight')
		current_output = 4.0
	'''
	return


def response(path,tags, args, source):
	print args[0]

	print "recieving"
	respond_motion(args[0])

		
	

server.addMsgHandler("/wek/outputs",response)

def each_frame():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()


        

def main():
    """This runs the protocol on port 8000"""
    
    while run:
    	time.sleep(1)
    	each_frame()
    server.close()

if __name__ == '__main__':
    main()

