#scatter_squares
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40, c = y_values, cmap = plt.cm.Blues, edgecolor="none")

#style the chart with a title etc

plt.title("Squares Scatter", fontsize = 24)
plt.xlabel("Number", fontsize = 14)
plt.ylabel("Square of Number", fontsize = 14)

#tick label sizes
plt.tick_params(axis="both", which="major", labelsize = 14)

#set the range for each axis
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches = 'tight')
plt.show()
