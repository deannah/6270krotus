"""
Figuring out motors.
"""

from RobotController import *
import time

robot = RobotController()

try:
	while(True):
		robot.driveForward()
		time.sleep(2)
		robot.driveBackward()
		time.sleep(2)
		robot.stop()
except KeyboardInterrupt:
	robot.off()
