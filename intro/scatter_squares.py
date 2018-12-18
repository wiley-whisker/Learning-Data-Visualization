import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values, s=40, edgecolor='none', c=y_values, cmap=plt.cm.Blues)
# Could also use c='red' or c=(0,0,0.8)
# See all colormaps available at matplotlib.org colormaps_reverence

# Set chart title and label axes
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=4)
plt.ylabel("Square of value", fontsize=4)

# Set the tick labels
plt.tick_params(axis='both',which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
