
from RobotController import *
import socket

class TeleopController:
	def __init__(self, robot):
		self.robot = robot
		self.port = 5000
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.bind(("", port))
		self.bias = 0.0 											# ~(1830 - 620.0 - 1240.0) / 610.0
		self.power = 0.0 											# ~(690 - 620.0) / 610.0
		print "waiting on port:", port

	def receive(self):
		data, addr = s.recvfrom(1024)
		data = int(data)
   		if (data < 1240):		#2470 to 1250 bias, hopefully 10 to 1230 power 
    		self.power = (data - 620.0) / 610.0
    		if (abs(self.power) < .1):
    			self.power = 0.0
    		self.execute('motor', [self.bias, self.power])
    	else if (data < 2480):
    		self.bias = (data - 1860.0) / 610.0
    		if (abs(self.bias) < .1):
    			self.bias = 0.0
    		self.execute('motor', [self.bias, self.power])
    	else if (data == 2491):
    		self.execute('door', 0)
    	else if (data == 2511):
    		self.execute('door', 1)
    	else if (data == 2531):
    		self.execute('arm', 1)
    	else if (data == 2551):
    		self.execute('arm', 0)
    	else if (data == 2601):
    		self.robot.activateIR()
    	else:
    		print 'wtf, man'

	def execute(self, inputType, value):
		#for motor, value=[bias,power]
		if inputType=='motor':
			self.robot.setMotors(value[0],value[1])
		else if inputType='door':
			if value==0:
				self.robot.closeDoor()
			else if value ==1:
				self.robot.openDoor()
			else:
				print 'whutisdoor??'
		else if inputType='arm':
			if value==0:
				self.robot.raiseArm()
			else if value ==1:
				self.robot.lowerArm()
			else:
				print 'whutisarm??'
		else if inputType=='ir':
			self.robot.activateIR()

	def stopAll(self): #TODO
		bot.stop()

