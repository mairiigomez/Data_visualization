from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6
die_1 = Die()
die_2 = Die()

# Changing in it for list comprenhension
results = [die_1.roll_die() + die_2.roll_die() for _ in range(1000)]

# Analize the results
frequencies = []
max_result = die_1.number_sides + die_2.number_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of Rolling two D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename='d6_d6.html')