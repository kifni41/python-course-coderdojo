import math
class Circle :

	def __init__(self, radius) :
		self.name = 'Square'
		self.radius = radius
	
	def calc_area(self) :
		return math.pi * self.radius * self.radius
