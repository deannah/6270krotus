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
		# except it is list in reverse order.
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
			node.y = random*self.field.getWidth()
			if (self.field.isPassable((x, y))):
				#TODO is that check enough or do we also need to check
				#robot size separately?
				return node

	def findNearestNode(self, target):
		# find node in path closest to target.
		nearestNode = self.nodes[0]
		nearestDist = 10000
		for n in self.nodes:
			dx = n.x - target.x
			dy = n.y - target.y
			dist = dx*dx + dy*dy
			if (dist < nearestDist):
				nearestDist = dist
				nearestNode = n
		return nearestNode

	def tracePath(self, current, target):
		# updates path in self.nodes from current to target
		# returns bool whether or not it succeeded
		dx = target.x - current.x
		dy = target.y - current.y
		dist = sqrt(dx*dx+dy*dy)
		# basically go to every point between current and target
		N = int(dist)
		for n in range(N):
			node = TreeNode()
			node.x = current.x + dx* float(n+1)/N
			if (not self.field.isPassable(node)):
				#TODO again, will field account for robot size?
				return False
			if (n+! == N):
				#this is actually target node
				node = target
			node.parent = current
			self.nodes.append(node)
			current = node
		return True


	def backTrace(self, current):
		# builds up path from parent node to current
		# important, path starts with final node and ends with first node.
		path = [current]
		while (current.parent not None):
			path.append(current.parent)
			current = current.parent
		return path
