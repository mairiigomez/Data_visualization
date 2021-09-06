"""In this script we'll create a class with is function that is going to create a random walk 
the this function is going to be call in the script rw_visual. 
A random walk describe random decisions eanch of them by any chance"""

from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self,num_points=5000):
        """Initialize attributes of the walk."""
        self.num_point = num_points

        # All walks start at (0 , 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Decide which direction to go and how far to go in that direction"""
        
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance
        return x_step
        

    def fill_walk(self):
        """Calculate all the point in the walk"""

        # Keep taking steps until the walk reaches the desired lenght
        while len(self.x_values) < self.num_point:

            x_step = self.get_step()
            y_step = self.get_step()
            
            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position 
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)