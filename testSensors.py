"""
Testing out sensor data from robot model.
"""

def testSensors(model):
	model.getGyroData()
	model.getLeftBumpData()
	model.getRightBumpData()

model = RobotModel()
testSensors(model)
