import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = list(range(0, 10))
y = list(range(-10, 0))

plt.plot(x,y)

plt.show()

a = [0, -100, 25, 67, -323]
b = [0, 3, 7, 3, 9]

plt.plot(a, b)

plt.show()

plt.hist(a)
plt.hist(b)

plt.show()