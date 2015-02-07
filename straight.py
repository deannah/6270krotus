"""
lolololol driving straight I'm sleepy
"""

from RobotController import *
from RobotModel import *
import time

robot = RobotController()
model = RobotModel()
correction = 0.0
value = .4

try:
	while(True):
		robot.drive(value, correction)
		time.sleep(1)
		offset = model.getGyroData()
		correction = .001(500-offset)
except KeyboardInterrupt:
	robot.off()
