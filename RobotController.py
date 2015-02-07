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
		self.s.enable(True)
		for i in range(1400, 700, -100):
			self.s.pulsewidth_us(i)
			time.sleep(.05)
		self.s.enable(False) #TODO mmmm should I disable now??

	def rotateHigh(self):
		self.s.enable(True)
		for i in range(800, 1500, 100):
			self.s.pulsewidth_us(i)
			time.sleep(.05)
		self.s.enable(False) #TODO prolly shouldn't here...

	def rotate(self, current, desired):
		# rotates servo from current location to desired location
		#current and desired should ideally be multiples of 100
		self.s.enable(True)
		step = 100
		if (abs(current-desired)<=150):
			step = 25
		if (current>desired):
			step*=-1
		for i in range(current, desired+step, step):
			self.s.pulsewidth_us(i)
			time.sleep(.05)
		self.s.enable(False)

class InfraLed:
	def __init__(self, pin):
		self.led = mraa.Gpio(pin)
		self.led.dir(mraa.DIR_OUT)
		self.led.write(0)

	def activateIR(self):
		self.led.write(1)

	def deactivateIR(self):
		self.led.write(0)

class RobotController:
	def __init__(self):
		self.ir = InfraLed(7)
		# set up the motors
		self.left = Motor(3, 11, 12)
		self.right = Motor(9, 8, 13)
		# set up the servos
		self.arm = Servo(6)
		self.door = Servo(5)
		# These bools are necessary to prevent repeated calls
		# that will freak out robot, mainly from Xbox controller
		self.armUp = False
		self.doorOpen = False

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
			self.left.forward(value)
		else:
			self.left.backward(-value)

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

	def operateDoor(self):
		# opens and closes door with 1 second pause
		self.openDoor()
		time.sleep(1)
		self.closeDoor()

	def operateArm(self):
		#raises and lowers arm with 1 second pause
		self.raiseArm()
		time.sleep(1)
		self.lowerArm()

	def openDoor(self):
		# rotate servo to open door, releasing balls.
		if (not self.doorOpen):
			self.doorOpen = True
			self.door.rotate(650, 800)
		else:
			pass

	def closeDoor(self):
		# rotate servo to close door.
		if (self.doorOpen):
			self.doorOpen = False
			self.door.rotate(800, 650)
		else:
			pass

	def raiseArm(self):
		# rotate servo to raise arm to put balls in box
		if (self.armUp == False):
			self.armUp = True
			#self.arm.rotateHigh()
			self.arm.rotate(800, 1100)
		else:
			pass

	def lowerArm(self):
		# rotate servo to lower arm to catch balls.
		if (self.armUp == True):
			self.armUp = False
			#self.arm.rotateLow()
			self.arm.rotate(1100, 800)
		else:
			pass

	def activateIR(self):
		self.ir.activateIR()

	def deactivateIR(self):
		self.ir.deactivateIR()
		
