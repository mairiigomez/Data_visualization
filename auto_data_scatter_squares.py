"""python Generating 1000 points for us and using scatter """
import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# Sending a tuple as a color RGB colors closer to 0 dark to 1 lighter
"ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)"

# Using color maps assing a color to lower values and a different to higher
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart tittle and label axes
ax.set_title("Square number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set the range for each axis minimun a maximum values for x and y 
ax.axis([0, 1100, 0, 1100000])

# this command show the figure right away
"plt.show()"

# This comand save the plot to a file
plt.savefig('squares_plot.png', bbox_inches='tight')