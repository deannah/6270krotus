"""
This is the lowest level controller of the robot. This actually manipulates the robot, it controls motors, servos, and the IR. All of these functions are called by LocalController.

Utilizes mraa library to interact with board.

TODO this might be prettier with motor and servo classes. mwoop. It totes will be. argh.
"""
import mraa

class RobotController:
	def __init__(self):
		# set up the motors
		self.left = mraa.Pwm(3) #TODO I didn't switch these, did I?
		self.left.period_us(700) #TODO make them forward instead of backward
		self.right = mraa.Pwm(9)
		self.right.period_us(700)
		self.leftBrake = mraa.Gpio(11) #TODO if I switched above, these are too
		self.leftBrake.dir(mraa.DIR_OUT)
		self.rightBrake = mraa.Gpio(8)
		self.rightBrake.dir(mraa.DIR_OUT)
		self.leftDir = mraa.Gpio(12)
		self.leftDir.dir(mraa.DIR_OUT)
		self.rightDir = mraa.Gpio(13)
		self.rightDir.dir(mraa.DIR_OUT)
		# set up the servos
		self.arm = mraa.Pwm(5)
		self.arm.period_ms(20)
		self.door = mraa.Pwm(6)
		self.door.period_ms(20)
		#TODO implement servos rotating.

	def leftMotor(value):
		self.left.enable(True)
		self.left.write(value)

	def rightMotor(value):
		self.right.enable(True)
		self.right.write(value)

	def stopLeft():
		self.left.write(0)
		self.left.enable(False) #TODO should I do this?

	def stopRight():
		self.right.write(0)
		self.right.enable(False)
