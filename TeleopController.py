
from RobotController import *
import socket

class TeleopController:
	def __init__(self, robot):
		self.robot = robot
		self.port = 5000
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.bind(("", self.port))
		self.bias = 0.0 											# ~(1830 - 620.0 - 1240.0) / 610.0
		self.power = 0.0 											# ~(690 - 620.0) / 610.0
		print "waiting on port:", self.port

	def receive(self):
		data, addr = self.s.recvfrom(1024)
		data = int(data)
		print data
		if (data < 1240):		#2470 to 1250 bias, hopefully 10 to 1230 power 
			self.power = (data - 650.0) / 610.0
			if (abs(self.power) < .4):
				self.power = 0.0
			print self.power
			self.execute('motor', [self.bias, self.power])
		elif (data < 2480):
			self.bias = (data - 1840.0) / 610.0
			print self.bias
			if (abs(self.bias) < .2):
				self.bias = 0.0
			self.execute('motor', [self.bias, self.power])
		elif (data == 2491):
			self.execute('door', 0)
		elif (data == 2511):
			self.execute('door', 1)
		elif (data == 2531):
			self.execute('arm', 1)
		elif (data == 2551):
			self.execute('arm', 0)
		elif (data == 2601):
			self.execute('ir', 0)
		elif (data == 2600):
			self.execute('ir', 1)
		else:
			print 'wtf, man'

	def execute(self, inputType, value):
		#for motor, value=[bias,power]
		if inputType=='motor':
			self.robot.setMotors(value[0],value[1])
		elif inputType=='door':
			if value==0:
				self.robot.closeDoor()
			elif value ==1:
				self.robot.openDoor()
			else:
				print 'whutisdoor??'
		elif inputType=='arm':
			if value==0:
				self.robot.raiseArm()
			elif value ==1:
				self.robot.lowerArm()
			else:
				print 'whutisarm??'
		elif inputType=='ir':
			if (value == 0):
				self.robot.activateIR()
			else:
				self.robot.deactivateIR()

	def stopAll(self): #TODO
		self.robot.stop()

