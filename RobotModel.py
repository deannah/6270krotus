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
class RobotModel:
	def __init__(self):
		self.position = (0.0,0.0)
		self.theta = 0.0
		self.velocity = 0.0

	def getGyroData(self):
		#TODO
		pass

	def getVPSdata(self):
		#TODO
		pass

	def getBumpData(self):
		#TODO
		pass

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
