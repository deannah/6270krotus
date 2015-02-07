"""
Keeps track of list of tasks. Uses LocalController to actually achieve tasks. Approximately working as a state machine... but also doing planning within each task
- Start
- Navigate to Dispenser
- Collect Balls
- Navigate to Goal
- Release Balls

hmmm might want a separate FieldModel...
"""
from LocalController import *
#from RRT import *

class GlobalController:
	def __init__(self, robotModel, fieldModel):
		self.robotModel = robotModel
		self.fieldModel = fieldModel
		self.localController = LocalController(robotModel)

	def execute(self):
		# this is the brains of the autonomy. It goes through
		# all of the steps of the competition.
		#TODO this prolly needs a time limit?

		# Step one, just drive straight.

		try:
			seconds = 5.0
			self.localController.driveStraight(seconds)
		except KeyboardInterrupt:
			self.localController.robot.off()
		"""
		# navigate to closest dispenser
			#find closest dispenser
		dispenser = (0, 0, 0) #assume dispenser is accurate, TODO
			#determine path, navigate along it.
		rrt = RRT(self.fieldModel)
		disPath = rrt.plan(self.robotModel.getPosition, dispenser, 100)
		for point in disPath.reverse():
			self.localController.navigate(point)
		# collect balls
		localController.collect()
		# navigate to goal
		goal = (0, 0, 0) # lol what is goal TODO
		goalPath = rrt.plan(self.robotModel.getPosition, goal, 100)
		for point in goalPath.reverse():
			self.localController.navigate(point)
		# release balls
		localController.release()
		"""
