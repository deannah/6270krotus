"""
testing out RobotController's servo functions,
figuring out good values for raiseArm, lowerArm, openDoor, closeDoor
"""

from RobotController import *
import time

robot = RobotController()

try:
	robot.raiseArm()
	time.sleep(2)
	robot.lowerArm()
except KeyboardInterrupt:
	robot.lowerArm()
