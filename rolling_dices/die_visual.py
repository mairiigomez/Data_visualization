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

print(frequencies)
