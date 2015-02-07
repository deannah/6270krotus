"""
testing out RobotController's servo functions,
figuring out good values for raiseArm, lowerArm, openDoor, closeDoor
"""

from RobotController import *
import time

robot = RobotController()

try:
	robot.openDoor()
	time.sleep(2)
	robot.closeDoor()
except KeyboardInterrupt:
	robot.closeDoor()
