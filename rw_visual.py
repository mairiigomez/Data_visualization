"""We wrote the Class RandomWalk in a different module random_walk.py"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active
while True:
    # Make a randomwalk instance 
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk 
    plt.style.use('classic')

    # resolution system passing dpi
    fig, ax = plt.subplots(figsize=(10,5), dpi=100)
    point_numbers = range(rw.num_point)

    # Create each point for the values of the instance 
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    # Emphasize the first and last points
    ax.scatter(0, 0, c='green',edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    # Keep running 
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break