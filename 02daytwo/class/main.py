"""
Main Program to calculate geometry using class
"""
import geometry.triangle as triangle

print('Main Program using Class')

t1 = triangle.Triangle(10,30)
print(t1.calc_area())
t1.draw()
t2 = triangle.Triangle(100,40)
print(t2.calc_area())
t2.draw()
t1.draw()
