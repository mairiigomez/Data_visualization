"""Ploting a simple line graph, giving it input and output values
title, labels, and using 'seaborn' style"""

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')

# Generate one or more plots in the same figure
# fig is the entire figure 
# ax represents a single plot
fig, ax = plt.subplots()
# plot data given in a meaningful way
# given the input and output values 
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes. 
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', labelsize=4)

plt.show()