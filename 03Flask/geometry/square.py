class Square :
	def __init__(self, side) :
		self.name = 'Square'
		self.side = side
	
	def calc_area(self) :
		return self.side * self.side
