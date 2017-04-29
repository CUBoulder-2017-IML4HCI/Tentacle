
import OSC

wek = OSC.OSCClient()
wek.connect(('127.0.0.1', 6448))


def orientation(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/wek/inputs")
    for elem in data[1:5]:
        elem = float(elem)
        oscmsg.append(elem)

    wek.send(oscmsg)
    print oscmsg
    #print oscmsg[1:]
    print(data)

def gyro(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    #print(data)

def pose(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    #print(data)

def accel(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    #print(data)

def emg(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    #print(data)
#myo = OSC.OSCClient()
#myo.connect(('127.0.0.1', 7777))
    
#msg = OSC.OSCMessage()


if __name__ == "__main__":
    myo = OSC.OSCServer(('127.0.0.1', 7777))
    myo.addMsgHandler('/myo/orientation', orientation)
    myo.addMsgHandler('/myo/gyro', gyro)
    myo.addMsgHandler('/myo/pose', pose)
    myo.addMsgHandler('/myo/accel', accel)
    myo.addMsgHandler('/myo/emg', emg)

    myo.serve_forever()
