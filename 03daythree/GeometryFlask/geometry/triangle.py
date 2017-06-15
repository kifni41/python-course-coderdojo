"""
Class : Triagle
Class : gabungan fungsi dan vaiable
"""


class Triangle:

    def __init__(self, bottom, height):
        self.name = 'Triangle'
        self.bottom = bottom
        self.height = height

    def calc_area(self):
        return self.bottom * self.height / 2


