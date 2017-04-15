from Stepper import Stepper
import time
import OSC

class Osc2Steppers:
    """Class that listens for OSC messages, and forwards them as target positions for stepper motors"""

    stepper_time_interval_seconds = 0.01

    def __init__(self, osc_ip='0.0.0.0', osc_port=12000):
        """Create our stepper object and osc server object"""

        self.debug = True

        # listen for OSC messages on port 12000 (Wekinator default)
        self.stepper_count = 2 #4

        # Pin order:             [ENB|MS1|MS2|MS3|RST|SLP|STP|DIR]
        self.stepper_A = Stepper([  4,  5,  6,  7,  0,  0,  3,  2],
            "Stepper A", self.stepper_time_interval_seconds)
        self.stepper_B = Stepper([ 10, 11, 12, 13,  0,  0,  9,  8],
            "Stepper B", self.stepper_time_interval_seconds)
        self.stepper_C = Stepper([ 16, 17, 18, 19,  0,  0, 15, 14],
            "Stepper C", self.stepper_time_interval_seconds)
        self.stepper_D = Stepper([ 22, 23, 24, 25,  0,  0, 21, 20],
            "Stepper D", self.stepper_time_interval_seconds)
        print "Created 4 steppers"

        self.OSCServer = OSC.OSCServer((osc_ip, osc_port))
        self.OSCServer.addMsgHandler('/wek/outputs', self.wek_outputs_handler)
        print "Tentacle Control is listening for OSC message /wek/outputs, ip %s port %s" % (osc_ip, osc_port)


    def go(self):
        """Start steppers self-updating, and start our OSC server listening"""
        #self.stepper_A.go()
        self.stepper_B.go()
        # self.stepper_C.go()
        self.stepper_D.go()
        self.OSCServer.serve_forever()

    def wek_outputs_handler(self, addr, tags, data, client_address):
        """Callback that is called when we receive an osc message with path '/wek/outputs'"""
        data[0] *= 150
        data[1] *= 150
        if self.debug:
            print "OSCMessage '%s' from %s: %s" % (addr, client_address, data)

        if (len(data) != self.stepper_count):
            print "Error: Expected %s OSC values, got %s" % (self.stepper_count, len(data))
            return

        # HERE'S THE MAGIC!
        # Pass on values to our stepper motors
        #self.stepper_A.move_to_position(data[0])
        self.stepper_B.move_to_position(data[0])
        #self.stepper_C.move_to_position(data[2])
        self.stepper_D.move_to_position(data[1])


if __name__ == "__main__":
    """We are being called directly--just start listening"""
    tentacle_listener = Osc2Steppers()
    tentacle_listener.go()
