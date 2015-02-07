"""
This sets everything up for the robot. Initializes model and GlobalController, and then begins the robot's competition code ( globalController.execute() )
"""
from RobotModel import *
from GlobalController import *

robotModel = RobotModel()
globalController = GlobalController(robotModel)

# Time to compete!

while True:
	# In case it manages to get through all the tasks, keep repeating
	globalController.execute()
