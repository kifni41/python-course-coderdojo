"""
Class : Triagle
Class : gabungan fungsi dan vaiable
"""
class Triangle :
	#Class variable, public to triangle class
	COUNT = 0

	def __init_(_self, bottom, height) :
		self.name = 'Triangle'
		self.bottom = bottom
		self.height = height
		Triangle.COUNT +=1
	
	def calc_area(self) :
		return self.bottom * self.height /2

	def draw(self) :
		print('Geometry Name :',self.name, 'Count=',Triangle.COUNT)
