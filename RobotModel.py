"""
This will contain modeling code, which will estimate position, theta
and velocity of robot.

Currently going to have this be a bit of a mess, but hopefully
we'll be able to make it more modular later.

Todo list:
- figure out how to get data
-- gyro
-- bump sensor left/right
-- VPS
- figure out how data is used to calculate position/etc.

"""
import mraa

# I think these have to be defined outside of the class...
def rightbump(args):
	# called when right bump sensor activated
	# also seems to get called several times in a row
	# when you stop pressing, which is a thing.
	print "Right bump just triggered"

def leftbump(args):
	# called when left bump sensor activated
	print "Left bump triggered"

class RobotModel:

	def __init__(self):
		self.position = (0.0,0.0)
		self.theta = 0.0
		self.velocity = 0.0
		self.gyro = mraa.Aio(0)
		self.left = mraa.Gpio(2)
		self.left.isr(mraa.EDGE_RISING, leftbump, leftbump)
		self.right = mraa.Gpio(4)
		self.right.isr(mraa.EDGE_RISING, rightbump, rightbump)

	def getGyroData(self):
		# pin A0
		# Gyro currently reading 50, 51, or 52
		# seemingly regardless of what robot is doing.
		value = self.gyro.read()
		print "Gyro reads: ", str(value)

	def getVPSdata(self):
		# team #, x, y, theta, and time, it's a function we'll call
		# this'll be a thread running in the background, ?
		#TODO
		pass

	def getLeftBumpData(self):
		# pin 2
		# self.left.read() returns bool 0 or 1 if pressed
		# this one might be derpy...
		value = self.left.read()
		print "Left bump reads: ", str(value)

	def getRightBumpData(self):
		# pin 4
		value = self.right.read()
		print "Right bump reads: ", str(value)

	def step(self):
		# Essentially, utilize gathered data to update values
		# this gets run every step... Or whenever there is new data?
		# I'm guessing former. Gives estimate of position and velocity
		# that controller will use
		#TODO
		pass

	def getPosition(self):
		return self.position

	def getTheta(self):
		return self.theta

	def getVelocity(self):
		return self.velocity
