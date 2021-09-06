from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6
die = Die()

results = []
# Make some rolls and store the result in a list
for roll_num in range(1000):
    result = die.roll_die()
    results.append(result)

# Analize the results
frequencies = []
for value in range(1,die.number_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, die.number_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of Rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename='d6.html')