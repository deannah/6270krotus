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

class GlobalController:
	def __init__(self, model):
		self.model = model
		self.localController = LocalController(model)

	def execute(self):
		# maybe it also has to be in charge of starting, for now assume not
		# navigate to closest dispenser
			#find closest dispenser
			#determine path, navigate along it.
		# collect balls
		localController.collect()
		# navigate to goal
		# release balls
		localController.release()
		#TODO
