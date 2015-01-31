
from RobotController import *

class TeleopController:
	def __init__(self, robot):
		self.robot=robot

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

