"""
This local controller completes individual tasks:
- navigate to a point (drive, turn, use PID control)
- operate servo1 (arm, rotate balls into box)
- operate servo2 (door, release balls into goal (hopefully goal))
- activate IR sensor

Gets position/etc estimates from RobotModel

Eventually implement some modularity. Especially want separate code
for motors and servos and things, but for now it can go in here I suppose.

Maybe thinking... AbstractLocalController with NavigateController and CollectController etc, GlobalController creates instance of wanted LocalController which operates until its task is complete...

On second thought, maybe I won't bother doing an abstract class.
"""
from pid import *

class LocalController:
	def __init__(self, model):
		self.model = model

	def navigate(self, goal):
		# use default pid. I'm assuming this is how GlobalController
		# will wind up calling navigate.
		ki = 0 #TODO
		kd = 0 #TODO
		kp = 0 #TODO
		pid = PID(ki, kd, kp)
		self.navigate(goal, pid)

	def navigate(self, goal, pid):
		# prolly this should return a bool whether it failed or succeeded, but for now you can assume no obstacles probably.
		(myX,myY)=self.model.getPosition()
		myTheta=self.model.getTheta()
		dx=goal[0]-myX
		dy=goal[1]-myY
		norm=sqrt(dx*dx+dy*dy)
		dx/=norm
		dy/=norm
		cross=dx*sin(myTheta)-dy*cos(myTheta)
		time=getTime()				#TODO
		power=pid.update(-cross,time)
		if(abs(cross)>0.5):
			bias=0.0
		else:
			bias=0.5
		setRightMotor(bias+power)
		setLeftMotor(bias-power)
		(myX,myY)=self.model.getPosition()
		dist=sqrt((goal[0]-myX)**2+(goal[1]-myY)**2)
		if(dist > 1):
			self.navigate(goal,pid)
		# goal in form (x, y, theta), probably
		# this is where some PID control happens
		# hopefully make use of some lower level code to set motors
		# at each step remember to step the model so it updates...
		#TODO
		pass
	def turnTo(self,angle,pid):
		myTheta=self.model.getTheta()
		cross = cos(angle) * sin(myTheta) - sin(angle) * cos(myTheta)
		time=getTime()
		power=pid.update(-cross,time)
		if (abs(diff)>0.1):
			setLeftMotor(power);		#TODO
			setRightMotor(-power); 	#TODO
			self.turnTo(angle)
	def collect(self):
		# Complete the action of collecting ping pong balls
		# Needs to activate IR sensor, and then activate servo1
		# rotate arm continually? or activate sensor, collect, then
		# rotate? repeat how many times?
		#TODO
		pass

	def release(self):
		# Complete the action of releasing the ping pong balls
		# Really just involves operating servo2
		self.openDoor()
		#TODO some kind of waiting
		self.closeDoor()

	def openDoor(self):
		# rotate servo2 to open door, figure out reasonable angle later
		#TODO
		pass

	def closeDoor(self):
		# rotate servo2 to close door, figure out angle later
		#TODO
		pass

"""class AbstractLocalController:
	def __init__(self, model):
		self.model = model

	def step():
		# work on completing goal.
		raise NotImplementedError

	def goalComplete():
		# check if goal completed. """
