from random import randint

class Die:
    """A class representing a single die"""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.number_sides = num_sides

    def roll_die(self):
        """Return a random value between 1 and number of side"""
        return randint(1, self.number_sides)
        
