"""
RRT - Rapidly Exploring Random Tree
This is how a lot of the robot's global planning will occur.

Heavily based upon sample RRT code provided by Ariel Wexler
"""

from random import random

class TreeNode:
	def __init__(self):
		self.x = 0.0
		self.y = 0.0
		self.parent = None
	def toString(self):
		return "Node: (" + str(self.x) + ", " + str(self.y)

class RRT:
	def __init__(self, field):
		self.nodes = []
		self.field = field

	def plan(self, start, end, attempts):
		# generates a path from start to end
		self.nodes = [start]
		while(attempts > 0):
			target = end
			if(random() < .7):
				target = self.generateTarget()
			nearestNode = self.findNearestNode(target)
			self.tracePath(nearestNode, target)
			if (end.parent != None):
				print("Search success.")
				return self.backTrace(end)
			attempts -= 1
		print("Search failure.")
		return []

	def generateTarget(self):
		# generates a random target
		while(True):
			node = TreeNode()
			node.x = random*self.field.getWidth()
