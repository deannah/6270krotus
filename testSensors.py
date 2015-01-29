"""
Testing out sensor data from robot model.
"""

from RobotModel import *
import time

def testSensors(model):
	model.getGyroData()
	model.getLeftBumpData()
	model.getRightBumpData()

model = RobotModel()

try:
	while True:
		testSensors(model)
		time.sleep(.1)

except KeyboardInterrupt:
	print "Ending test session"
