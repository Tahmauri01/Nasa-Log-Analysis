import matplotlib.pyplot as plt

categories = ['apples','bananas','oranges', 'pear', 'kiwi']

numbers = [61, 14, 77, 39, 56]

plt.bar(categories, numbers, color = ['red', 'yellow', 'orange', 'green', 'brown'])

plt.show()