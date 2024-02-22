import plotly.express as px

from die import Die

# Create one D6 die, one D12, and one D20.
die_1 = Die()
die_2 = Die(12)
die_3 = Die(20)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1500):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of Rolling One D6, One D12, and One D20 Dice 1500 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)            
fig.show()