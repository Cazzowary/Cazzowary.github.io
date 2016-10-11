#die
from random import randint

class Die():
    """create a die class"""
    def __init__(self, num_sides = 6):
        """assume a 6 sided die"""
        self.num_sides = num_sides

    def roll(self):
        """return random val between 1 and 6"""
        return randint(1, self.num_sides)
