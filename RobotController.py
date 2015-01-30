"""
This is the lowest level controller of the robot. This actually manipulates the robot, it controls motors, servos, and the IR. All of these functions are called by LocalController.

Utilizes mraa library to interact with board. That code was largely written by Chris and Crystal, but I'm putting it together in one place.

TODO this might be prettier with motor and servo classes. mwoop. It totes will be. argh.
"""
import mraa
import time

class Motor:
	def __init__(self, pin, brake, direction):
		self.m = mraa.Pwm(pin)
		self.m.period_us(700)
		self.brake = mraa.Gpio(brake)
		self.brake.dir(mraa.DIR_OUT)
		self.dir = mraa.Gpio(direction)
		self.dir.dir(mraa.DIR_OUT)

	def write(self, value):
		self.m.enable(True) #TODO should this be in init?
		self.m.write(value)

	def stop(self, value):
		self.m.write(0)
		self.m.enable(False) #TODO should I do this?

class Servo:
	def __init__(self, pin):
		self.s = mraa.Pwm(pin)
		self.s.period_ms(20)

	def rotateLow(self):
		#this assumes it is already high...
		# might just want one rotate function? TODO
		self.s.enable(True) #TODO still questioning enabling.
		for i in range(2100, 700, -100):
			self.s.pulsewidth_us(i)
			time.sleep(.05)
		self.s.enable(False)

	def rotateHigh(self):
		self.s.enable(True)
		for i in range(800, 2300, 100):
			self.s.pulsewidth_us(i)
			time.sleep(.05)
		self.s.enable(False)

	def rotate(self, value):
		self.s.enable(True)
		# probably need to find current theta?
		# basically mimic the above but from current to value
		#TODO
		pass

class RobotController:
	def __init__(self):
		# set up the motors
		self.left = Motor(3, 11, 12) #TODO did I switch?
		self.right = Motor(9, 8, 13)
		# set up the servos
		self.arm = Servo(5) #TODO did I switch these pins?
		self.door = Servo(6)

	def openDoor(self):
		# rotate servo to open door, releasing balls.
		#TODO
		pass

	def closeDoor(self):
		# rotate servo to close door.
		#TODO
		pass

	def raiseArm(self):
		# rotate servo to raise arm to put balls in box
		#TODO
		pass

	def lowerArm(self):
		# rotate servo to lower arm to catch balls.
		#TODO
		pass

	def activateIR(self):
		# turn on IR to activate dispensers
		#TODO
		pass
