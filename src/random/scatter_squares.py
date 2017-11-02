import matplotlib.pyplot as plt

x_valuse = list(range(1, 1001))
y_valuse = [x**2 for x in x_valuse]

plt.scatter(x_valuse, y_valuse, c=y_valuse, cmap=plt.cm.Blues,
    edgecolor='none', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

#plt.show()
plt.savefig('1square_plot.png', bbox_inches='tight')
