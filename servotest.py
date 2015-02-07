"""
testing out RobotController's servo functions,
figuring out good values for raiseArm, lowerArm, openDoor, closeDoor
"""

from RobotController import *
import time

robot = RobotController()

try:
	robot.operateArm()
	time.sleep(1)
	robot.operateDoor()
except KeyboardInterrupt:
	robot.closeDoor()
	robot.lowerArm()
