"""We wrote the Class RandomWalk in a different module random_walk.py"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active
while True:
    # Make a randomwalk instance 
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk 
    plt.style.use('classic')
    fig, ax = plt.subplots()

    # Create each point for the values of the instance 
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    # Keep running 
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break