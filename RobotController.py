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
		self.m.enable(True)
		self.brake = mraa.Gpio(brake)
		self.brake.dir(mraa.DIR_OUT)
		self.brake.write(0)
		self.dir = mraa.Gpio(direction)
		self.dir.dir(mraa.DIR_OUT)

	def forward(self, value):
		self.dir.write(1)
		self.m.write(value)

	def backward(self, value):
		self.dir.write(0)
		self.m.write(value)

	def stop(self):
		self.brake.write(1)
		self.m.write(0)
		self.brake.write(0)

	def off(self):
		self.stop()
		self.m.enable(False)

class Servo:
	def __init__(self, pin):
		self.s = mraa.Pwm(pin)
		self.s.period_ms(20)

	def rotateLow(self):
		#this assumes it is already high...
		# might just want one rotate function? TODO
		self.s.enable(True)
		for i in range(2100, 700, -100):
			self.s.pulsewidth_us(i)
			time.sleep(.05)
		self.s.enable(False) #TODO mmmm should I disable now??

	def rotateHigh(self):
		self.s.enable(True)
		for i in range(800, 2300, 100):
			self.s.pulsewidth_us(i)
			time.sleep(.05)
		self.s.enable(False) #TODO prolly shouldn't here...

	def rotate(self, value):
		self.s.enable(True)
		# probably need to find current theta?
		# basically mimic the above but from current to value
		#TODO this might be impossible....
		pass

class InfraLed:
	def __init__(self, pin):
		self.led = mraa.Gpio(pin)
		self.led.dir(mraa.DIR_OUT)
		self.led.write(0)

	def activate(self):
		self.led.write(1)
		time.sleep(100)
		self.led.write(0)

class RobotController:
	def __init__(self):
		self.ir = InfraLed(7)
		# set up the motors
		self.left = Motor(3, 11, 12)
		self.right = Motor(9, 8, 13)
		# set up the servos
		#self.arm = Servo(5) #TODO did I switch these pins?
		#self.door = Servo(6)

	def driveForward(self):
		#This and driveBackward are probably unnecessary
		#because we'll be driving left and right separately.
		#TODO remove them or maybe rewrite them w/ bias
		self.left.forward(.4)
		self.right.forward(.4)

	def driveBackward(self):
		self.left.backward(.4)
		self.right.backward(.4)

	def setMotors(self,bias,power):
		if bias+power > 0:
			self.right.forward(bias+power)
		else:
			self.right.backward(-bias-power)
		if bias-power > 0:
			self.left.forward(bias-power)
		else:
			self.left.backward(power-bias)

	def setLeftMotor(self,value):
		if value > 0:
			self.left.forward(.8 * value)
		else:
			self.left.backward(-.8 * value)

	def setRightMotor(self,value):
		if value > 0:
			self.right.forward(value)
		else:
			self.right.backward(-value)

	def stop(self):
		self.left.stop()
		self.right.stop()

	def off(self):
		# meant for turning motors off
		self.left.off()
		self.right.off()

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
		self.ir.activate()
		