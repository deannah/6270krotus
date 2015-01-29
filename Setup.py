"""
This sets everything up for the robot. Initializes model and GlobalController, then waits for start and begins the robot's competition code ( globalController.execute() )
"""
from RobotModel import *
from GlobalController import *

robotModel = RobotModel()
globalController = GlobalController(robotModel)

# while VPS data is nonexistant, wait
while not robotModel.getVPSdata():
	#basically wait
# Time to compete!
globalController.execute()
