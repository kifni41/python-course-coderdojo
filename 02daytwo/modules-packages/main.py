"""
This program will calculate triangle area using the formula
area = height * borrom /2
"""

import geometry.triangle as triangle
import geometry.square as square
import geometry.circle as circle

print('Main Program')

print('Triagle Area : ',triangle.calc_triangle_area(10,5))
print('Square Area : ',square.calc_square_area(4))
print('Circle Area : ',circle.calc_circle_area(7))
