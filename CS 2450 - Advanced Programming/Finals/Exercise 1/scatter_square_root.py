import matplotlib.pyplot as plt
from math import sqrt

x_values = range(200, 100, -10)
y_values = [sqrt(x) for x in x_values]

#plt.style.use('reverse')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=25)

# Set chart title and label axes.
ax.set_title("Square Root of every 10th Value between 200 and 100 in descending order.", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square Root of Value", fontsize=14)

# Set size of tick labels and show both x and y with x_values and y_values, respectively.
ax.tick_params(labelsize=14, axis='both')
ax.set_xticks(x_values)
ax.set_yticks(y_values)

ax.invert_xaxis()

plt.show()