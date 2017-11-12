import OSC
import time

def handler(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)

if __name__ == "__main__":

	s = OSC.OSCServer(('192.168.2.101', 12289))  # listen on localhost, port 57120
	s.addMsgHandler('/magic_hat', handler)     # call handler() for OSC messages received with the /startup address
	s.addMsgHandler('/bird_cage', handler) 
	s.addMsgHandler('/black_board', handler)
	s.serve_forever()



	# c = OSC.OSCClient()
	# c.connect(('192.168.2.9',12211))

	# try:
	# 	while True:
	# 		print "send"
	# 		oscmsg = OSC.OSCMessage()
	# 		oscmsg.setAddress("/endup")
	# 		oscmsg.append('HELLO')
	# 		c.send(oscmsg)
	# 		time.sleep(1)
	# except ValueError: pass

