"""
This is a model of the field. Soon this will account for the fact that the field is a hexagon. Not an all purpose model by any means.

I'm too tired for this.

I know there will be an inner hexagon... Should I just let it bump into it?

Ideally this would also keep track of your side, where your goal is, and where your dispensers are. But how??? TODO
- self.dispensers [(x, y), (x, y), (x, y)] and then a function to tell you if a position is close to one of those?
- goal might be definable only if inner hexagon hard coded...
"""

class FieldModel:
	def __init__(self):
		#TODO I assume width and height will be fixed?
		#IT'S A HEXAGON. I DON'T WANT TO DEAL WITH THAT.
		self.width = 0
		self.height = 0
		# In theory grid will keep track of whether point is passable or not.
		self.grid = [[True]*width]*height

	def updatePosition(self, position, clear):
		# clear is boolean, False if not passable, True if passable
		self.grid[position[0]][position[1]] = clear

	def isPassable(self, position)
		# returns bool whether position is passable
		#TODO should I account for robot size here or elsewhere? Lol.
		return self.grid[position[0]][position[1]]

	def getHeight(self)
		return self.height

	def getWidth(self)
		return self.width
