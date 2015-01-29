"""
Testing out sensor data from robot model.
"""

from RobotModel import *

def testSensors(model):
	model.getGyroData()
	model.getLeftBumpData()
	model.getRightBumpData()

model = RobotModel()
testSensors(model)
