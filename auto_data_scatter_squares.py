"""python Generating 1000 points for us and using scatter """
import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart tittle and label axes
ax.set_title("Square number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set the range for each axis minimun a maximum values for x and y 
ax.axis([0, 1100, 0, 1100000])

plt.show()